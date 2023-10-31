from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
# Lấy giá trị của biến môi trường từ tệp .env
openai_api_key = os.getenv('OPENAI_API_KEY')

# Multiple PDFs
def get_pdfs_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        text += get_pdf_text(pdf)
    return text

# Single PDF
def get_pdf_text(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

prompt = """You are an AI assistant created by Phenikaa University to answer questions about the university and have friendly conversations with students. 
Your goal is to be helpful, exaclly. 
If you can't find the information, say you don't know. Don't try to make up answers.
Please using Vietnamese"""

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(temperature= 0.5, model_name= "gpt-3.5-turbo-16k")
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    return conversation_chain

pdf = get_pdfs_text(["./pdf/Thoi khoa bieu Tuan SHCD K15- Ngày 15.9.2021.pdf", "./pdf/ctdtict1-1.pdf", "./pdf/Thông báo về việc xin miễn giảm và nộp học phí .pdf", "./pdf/Tb_ra_vao_cong.pdf"])
chunks = get_text_chunks(pdf)
vec = get_vectorstore(chunks)

def main():
    history = []
    while(True):
        question = input("Nhập câu hỏi: ")
        result = get_conversation_chain(vec)({"question": (prompt + question)})
        history.append((question, result["answer"]))
        print(history)
main()
    