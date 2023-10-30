import streamlit as st
from dotenv import load_dotenv
import pickle 
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = '8d995ee2e1b43236aaea002c'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push() 
from chatPDF import routes
# from chatPDF.models import User, Topic, Conversation

# login_manager = LoginManager(app)