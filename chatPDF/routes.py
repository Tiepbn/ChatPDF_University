from chatPDF import app 
from flask import render_template, redirect, url_for, request
# from chatPDF.form import RegisterForm

@app.route('/')
@app.route('/home')
def home():  
    return render_template('home_chatbot.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/sigup')
def sigup():
    return render_template('sigup.html')

@app.route('/baseuser')
def baseuser():
    return render_template('baseuser.html')

@app.route('/usernotaccount')
def usernotaccount():
    return render_template('usernotaccount.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        pdf = request.files['pdf']
        if pdf:
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text=text)

            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            store_name = pdf.filename[:-4]
            
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)
            
            return "File processed successfully!"
    return render_template('admin.html')


 