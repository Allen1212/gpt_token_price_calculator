import streamlit as st
from components.sidebar import sidebar
from utils import parse_docx, parse_pdf, parse_txt, count_tokens


st.set_page_config(
    page_title="GPT Token Price Calculator", page_icon="📟", layout="wide"
)
st.header("📟GPT Token Price Calculator")

sidebar()


def clear_submit():
    st.session_state["submit"] = False


uploaded_file = st.file_uploader(
    "Upload a pdf, docx, or txt file",
    type=["pdf", "docx", "txt"],
    help="Only support pdf, docx, and txt format!",
    on_change=clear_submit,
)

uploaded = False
doc = None

if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        doc = parse_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        doc = parse_docx(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        doc = parse_txt(uploaded_file)
    else:
        raise ValueError("File type not supported!")

    uploaded = True

prompt = st.text_area("Add your prompt:", on_change=clear_submit)
st.session_state["PROMPT"] = prompt
button = st.button("Calculate")

if button or st.session_state.get("submit"):
    if not uploaded:
        st.error("Please upload a document!")
    else:
        st.session_state["submit"] = True
        length, price = count_tokens(doc)
        st.markdown(f"#### 🔢Tokens: :green[{length}]")
        st.markdown(f"#### 💵Price: :green[${price:g}]")
