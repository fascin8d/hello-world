"""RAG function calling: search document chunks via ChromaDB."""

import voyageai
from chromadb import Collection
from pipecat.adapters.schemas.function_schema import FunctionSchema
from pipecat.adapters.schemas.tools_schema import ToolsSchema
from pipecat.frames.frames import FunctionCallResultProperties
from pipecat.services.llm_service import FunctionCallParams

EMBEDDING_MODEL = "voyage-3-lite"

search_document_schema = FunctionSchema(
    name="search_document",
    description=(
        "Search the loaded document for information relevant to the user's question. "
        "Always use this before answering questions about the document."
    ),
    properties={
        "query": {
            "type": "string",
            "description": "The search query to find relevant information in the document",
        },
    },
    required=["query"],
)

tools = ToolsSchema(standard_tools=[search_document_schema])


def create_search_handler(collection: Collection, voyage_client: voyageai.Client):
    """Create a function-call handler that searches the document collection."""

    async def search_document_handler(params: FunctionCallParams):
        query = params.arguments.get("query", "")

        # Embed with input_type="query" for better retrieval
        query_embedding = voyage_client.embed(
            [query], model=EMBEDDING_MODEL, input_type="query"
        ).embeddings

        results = collection.query(
            query_embeddings=query_embedding,
            n_results=5,
            include=["documents", "distances"],
        )

        documents = results["documents"][0] if results["documents"] else []
        context = "\n\n---\n\n".join(documents)

        await params.result_callback(
            {"relevant_context": context, "num_results": len(documents)},
            properties=FunctionCallResultProperties(run_llm=True),
        )

    return search_document_handler
