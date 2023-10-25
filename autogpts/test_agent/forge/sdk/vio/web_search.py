from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.retrievers.web_research import WebResearchRetriever

import os

os.environ[
    "GOOGLE_API_KEY"
] = "AIzaSyCGsA_58qQ-HLXwFROo8NA-nIpO13zLBgk"  # Get it at https://console.cloud.google.com/apis/api/customsearch.googleapis.com/credentials
os.environ[
    "GOOGLE_CSE_ID"
] = "a5f084cd4ac78448d"  # Get it at https://programmablesearchengine.google.com/


# Vectorstore
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore import InMemoryDocstore

embeddings_model = OpenAIEmbeddings()
embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore_public = FAISS(
    embeddings_model.embed_query, index, InMemoryDocstore({}), {}
)

# LLM
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0, streaming=False)

# Search
from langchain.utilities import GoogleSearchAPIWrapper

search = GoogleSearchAPIWrapper()

# Initialize
web_retriever = WebResearchRetriever.from_llm(
    vectorstore=vectorstore_public, llm=llm, search=search, num_search_results=3
)


qa_chain = RetrievalQAWithSourcesChain.from_chain_type(llm, retriever=web_retriever)
print("Asking question.")
result = qa_chain({"question": "What is the best performing AI agent"})
print(result)
