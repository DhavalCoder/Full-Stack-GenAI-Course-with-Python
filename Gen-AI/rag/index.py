import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from langchain_core.embeddings import Embeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore



load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

if not NVIDIA_API_KEY:
    raise ValueError("NVIDIA_API_KEY not found in .env file")


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



pdf_path = Path(__file__).parent / "FOC_BARAPATE.PDF"

loader = PyPDFLoader(
    file_path=pdf_path
)

docs = loader.load()

print(f"Loaded {len(docs)} pages")



text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(
    documents=docs
)

print(f"Created {len(chunks)} chunks")



embedding_model = NVIDIAEmbeddings()


vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning-rag",
)

print("Indexing of Documents done....")