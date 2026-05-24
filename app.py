import streamlit as st
import ollama
from pypdf import PdfReader

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Offline Multimodal RAG",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}

.chat-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #1E1E1E;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🤖 Offline Multimodal RAG Assistant")
st.subheader("Upload PDFs and ask questions")

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

    # Read only first 5 pages for speed
    for page in reader.pages[:5]:
        text = page.extract_text()
        if text:
            pdf_text += text

    st.success("✅ PDF uploaded successfully")

# ---------------- QUESTION INPUT ----------------
question = st.text_input("Ask a question from your PDF")

# ---------------- PROCESS QUESTION ----------------
if question and pdf_text:

    prompt = f"""
    Use the following PDF content to answer the question.

    PDF Content:
    {pdf_text[:4000]}

    Question:
    {question}

    Give a short and clear answer.
    """

    try:
        with st.spinner("🤔 Thinking..."):

            response = ollama.generate(
                model="llama3",
                prompt=prompt
            )

        # Display Question
        st.markdown(f"""
        <div class="chat-box">
        <b>🙋 You:</b> {question}
        </div>
        """, unsafe_allow_html=True)

        # Display Answer
        st.markdown(f"""
        <div class="chat-box">
        <b>🤖 AI:</b> {response['response']}
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error("❌ Ollama is not running.")
        st.code("ollama run llama3")

elif question and not uploaded_file:
    st.warning("⚠ Please upload a PDF first")