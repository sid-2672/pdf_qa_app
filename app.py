import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ✅ This is the missing function — must be ABOVE where it's used
def load_document(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)

# 🚀 Streamlit App
st.title("📄 AI-Powered Document Q&A (Local)")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    temp_file = "./temp.pdf"
    with open(temp_file, "wb") as f:
        f.write(uploaded_file.read())

    st.info("Processing document... ⏳")

    chunks = load_document(temp_file)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(chunks, embeddings)
    retriever = vector_db.as_retriever()

    llm = Ollama(model="llama3")  # Or use "mistral", etc.

    system_prompt = (
        "You are a helpful assistant. Use the given context to answer the question. "
        "If you don't know the answer, say you don't know. "
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    qa_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, qa_chain)

    question = st.text_input("Ask a question about the document:")
    if question:
        response = chain.invoke({"input": question})["answer"]
        st.success(response)
    st.balloons()   