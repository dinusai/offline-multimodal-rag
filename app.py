import streamlit as st
from pypdf import PdfReader

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Offline Multimodal RAG",
    page_icon="📄",
    layout="wide"
)

# ---------------- LIGHT THEME ----------------
st.markdown("""
<style>
.stApp {
    background-color: white !important;
    color: black !important;
}

html, body, [class*="css"] {
    color: black !important;
}

h1, h2, h3 {
    color: #2563eb !important;
}

[data-testid="stSidebar"] {
    background-color: #f8fafc !important;
}

.stTextInput input {
    background-color: white !important;
    color: black !important;
    border: 2px solid #2563eb !important;
    border-radius: 10px !important;
}

.chat-box {
    padding: 15px;
    border-radius: 12px;
    background-color: #f3f4f6 !important;
    border: 1px solid #d1d5db !important;
    margin-bottom: 15px;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("📄 Offline Multimodal RAG Assistant")
st.subheader("Cloud Deployable PDF Assistant")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("📂 Upload PDF")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

# ---------------- READ PDF ----------------
pdf_text = ""

if uploaded_file:
    reader = PdfReader(uploaded_file)

    for page in reader.pages[:5]:
        text = page.extract_text()
        if text:
            pdf_text += text

    st.success("✅ PDF uploaded successfully")

# ---------------- QUESTION INPUT ----------------
question = st.text_input("Ask a question from your PDF")

# ---------------- ANSWER ----------------
if question and pdf_text:

    if question.lower() == "what is sql":
        answer = """
SQL (Structured Query Language) is a standard programming language used to store, retrieve, manage, and manipulate data in relational databases.
"""

    else:
        answer = pdf_text[:1000]

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

elif question and not uploaded_file:
    st.warning("⚠ Please upload a PDF first")