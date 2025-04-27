import os
import argparse
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="enter the path to the PDF document you'd like to load")
args = parser.parse_args()

# Confirm that the OPENAI_API_KEY is set
if not os.environ.get("OPENAI_API_KEY"):
    print("The OPENAI_API_KEY environment variable must be set before running the application")
    sys.exit(0)

# Load the specified PDF document
loader = PyPDFLoader(
    args.file_path,
    mode="page",
)

textbook_pages = loader.load()

print(len(textbook_pages))
print(textbook_pages[0].metadata)
print(textbook_pages[0].page_content)

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

db = Chroma.from_documents(
   textbook_pages,
   embedding=embeddings_model,
   persist_directory="../chroma_db"
)

results = db.similarity_search(
   "Which areas have little water?"
)

for result in results:
   print("\n")
   print(result.page_content)