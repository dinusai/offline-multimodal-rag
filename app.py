import streamlit as st
from pypdf import PdfReader

# Page setup
st.set_page_config(
    page_title="Offline Multimodal RAG",
    page_icon="📄",
    layout="wide"
)

# Theme
st.markdown("""
<style>
.stApp {
    background-color: white;
    color: black;
}
.chat-box {
    padding: 15px;
    border-radius: 12px;
    background-color: #f3f4f6;
    border: 1px solid #d1d5db;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📄 Offline Multimodal RAG Assistant")
st.subheader("Cloud Deployable PDF Assistant")

# Sidebar
with st.sidebar:
    st.header("📂 Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

pdf_text = ""

if uploaded_file:
    reader = PdfReader(uploaded_file)

    for page in reader.pages[:5]:
        text = page.extract_text()
        if text:
            pdf_text += text

    st.success("✅ PDF uploaded successfully")

question = st.text_input("Ask a question from your PDF")

if question and pdf_text:

    # Basic keyword search
    if question.lower() in pdf_text.lower():
        answer = "The answer is found in the uploaded PDF."

    elif "python" in question.lower():
        answer = "Python is a high-level, interpreted programming language known for simplicity and readability."

    elif "sql" in question.lower():
        answer = "SQL (Structured Query Language) is used to manage and query relational databases."

    else:
        answer = "This question is not directly found in the uploaded PDF."

    st.markdown(f"""
    <div class="chat-box">
    <b>🙋 You:</b> {question}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="chat-box">
    <b>🤖 AI:</b> {answer}
    </div>
    """, unsafe_allow_html=True)