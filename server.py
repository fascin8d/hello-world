"""Entry point: ingest a document, create a Daily room, and start the voice agent."""

import argparse
import asyncio
import os

import aiohttp
from pipecat.pipeline.runner import PipelineRunner
from pipecat.transports.daily.utils import DailyRESTHelper, DailyRoomParams

from bot import create_pipeline
from ingest import ingest


async def main():
    parser = argparse.ArgumentParser(description="Voice Document Agent")
    parser.add_argument("--pdf", help="Path to a PDF file to discuss")
    parser.add_argument("--url", help="URL to discuss")
    parser.add_argument("--room-url", help="Daily room URL (auto-created if omitted)")
    args = parser.parse_args()

    if not args.pdf and not args.url:
        parser.error("Provide --pdf <path> or --url <url>")

    source = args.pdf or args.url
    collection, voyage_client = ingest(source)

    async with aiohttp.ClientSession() as session:
        helper = DailyRESTHelper(
            daily_api_key=os.getenv("DAILY_API_KEY"),
            daily_api_url="https://api.daily.co/v1",
            aiohttp_session=session,
        )

        if args.room_url:
            room_url = args.room_url
        else:
            room = await helper.create_room(DailyRoomParams())
            room_url = room.url

        token = await helper.get_token(room_url)

        print(f"\n{'=' * 50}")
        print(f"  Join the conversation: {room_url}")
        print(f"{'=' * 50}\n")

        task, transport = create_pipeline(room_url, token, collection, voyage_client)

        runner = PipelineRunner()
        await runner.run(task)


if __name__ == "__main__":
    asyncio.run(main())
