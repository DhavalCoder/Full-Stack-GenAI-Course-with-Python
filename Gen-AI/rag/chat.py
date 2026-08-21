import os

from dotenv import load_dotenv
from openai import OpenAI

from langchain_core.embeddings import Embeddings
from langchain_qdrant import QdrantVectorStore



load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

if not NVIDIA_API_KEY:
    raise ValueError("NVIDIA_API_KEY not found in .env")


class NVIDIAEmbeddings(Embeddings):

    def __init__(self):
        self.client = OpenAI(
            api_key=NVIDIA_API_KEY,
            base_url="https://integrate.api.nvidia.com/v1"
        )

        self.model = "nvidia/nv-embedqa-e5-v5"

    def embed_documents(self, texts):
        response = self.client.embeddings.create(
            model=self.model,
            input=texts,
            extra_body={
                "input_type": "passage"
            }
        )

        return [
            item.embedding
            for item in response.data
        ]

    def embed_query(self, text):
        response = self.client.embeddings.create(
            model=self.model,
            input=text,
            extra_body={
                "input_type": "query"
            }
        )

        return response.data[0].embedding



embedding_model = NVIDIAEmbeddings()

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning-rag",
    embedding=embedding_model
)


user_query = input("Ask Something: ")


search_results = vector_db.similarity_search(
    query=user_query,
    k=4
)

context = "\n\n\n".join(
    [ 
        f"Page Content: {result.page_content}\n"
        f"Page Number: {result.metadata.get('page', 'Unknown')}\n"
        f"File Location: {result.metadata.get('source', 'Unknown')}"
        for result in search_results
    ]
)



SYSTEM_PROMPT = f"""
You are a helpful AI assistant who answers user questions
based only on the context retrieved from a PDF.

Answer the user's question using only the provided context.

If the answer cannot be found in the context,
say that you don't know based on the provided document.

When possible, mention the relevant page number so the user
can open the PDF and read more.

Context:

{context}
"""


llm_client = OpenAI(
    api_key=NVIDIA_API_KEY,
    base_url="https://integrate.api.nvidia.com/v1"
)

response = llm_client.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_query
        }
    ],
    temperature=0.2,
    max_tokens=1024
)

print("\n🤖:", response.choices[0].message.content)