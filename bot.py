"""Pipecat voice pipeline: Deepgram STT → Claude → Cartesia TTS over Daily WebRTC."""

import os

import voyageai
from chromadb import Collection
from pipecat.audio.vad.silero import SileroVADAnalyzer
from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.task import PipelineTask
from pipecat.processors.aggregators.openai_llm_context import OpenAILLMContext
from pipecat.services.anthropic.llm import AnthropicLLMService
from pipecat.services.cartesia.tts import CartesiaTTSService
from pipecat.services.deepgram.stt import DeepgramSTTService
from pipecat.transports.daily.transport import DailyTransport, DailyParams

from rag import create_search_handler, tools

SYSTEM_PROMPT = """\
You are a voice assistant that helps users understand and discuss a document.
Use the search_document function to find relevant information before answering.
Keep responses concise and conversational — 2-3 sentences max.
If you can't find the answer in the document, say so honestly.\
"""


def create_pipeline(
    room_url: str,
    token: str,
    collection: Collection,
    voyage_client: voyageai.Client,
) -> tuple[PipelineTask, DailyTransport]:
    """Build and return the Pipecat pipeline task and transport."""

    transport = DailyTransport(
        room_url=room_url,
        token=token,
        bot_name="Doc Agent",
        params=DailyParams(
            audio_out_enabled=True,
            vad_enabled=True,
            vad_analyzer=SileroVADAnalyzer(),
        ),
    )

    stt = DeepgramSTTService(api_key=os.getenv("DEEPGRAM_API_KEY"))

    llm = AnthropicLLMService(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        model="claude-sonnet-4-5-20250929",
    )

    tts = CartesiaTTSService(
        api_key=os.getenv("CARTESIA_API_KEY"),
        voice_id=os.getenv("CARTESIA_VOICE_ID", "79a125e8-cd45-4c13-8a67-188112f4dd22"),
    )

    # Register RAG function
    llm.register_function("search_document", create_search_handler(collection, voyage_client))

    # Play filler while searching
    @llm.event_handler("on_function_call_start")
    async def on_function_call_start(llm, function_name):
        await tts.say("Let me check the document.")

    # Conversation context with tools
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    context = OpenAILLMContext(messages, tools=tools)
    context_aggregator = llm.create_context_aggregator(context)

    pipeline = Pipeline(
        [
            transport.input(),
            stt,
            context_aggregator.user(),
            llm,
            tts,
            transport.output(),
            context_aggregator.assistant(),
        ]
    )

    task = PipelineTask(pipeline)
    return task, transport
