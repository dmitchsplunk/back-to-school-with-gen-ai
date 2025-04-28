import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Confirm that the OPENAI_API_KEY is set
if not os.environ.get("OPENAI_API_KEY"):
    print("The OPENAI_API_KEY environment variable must be set before running the application")
    sys.exit(0)

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings_model
)

llm = init_chat_model("gpt-4o-mini", model_provider="openai")

prompt = ChatPromptTemplate.from_template("You are an assistant for question-answering tasks. Use "
    + "the following pieces of retrieved context to answer the question. If you don't know the answer, "
    + "just say that you don't know. Use three sentences maximum and keep the answer concise.\n"
    + "Question: {question}\n"
    + "Context: {context}\n"
    + "Answer:")

example_messages = prompt.invoke(
    {"context": "The amount of water in an ecosystem affects its living things. Areas with little water, such as deserts, have fewer kinds of living things living there. ", "question": "Which areas have little water?"}
).to_messages()

assert len(example_messages) == 1
print(example_messages[0].content)
print(example_messages[0])

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}

# Compile application and test
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

#response = graph.invoke({"question": "Which areas have little water?"})
response = graph.invoke({"question": "Please create a question that asks how populations in a community survive"})
print(response["answer"])