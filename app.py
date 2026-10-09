import os

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAIError
from streamlit.errors import StreamlitSecretNotFoundError


def get_api_key() -> str | None:
    try:
        return os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
    except StreamlitSecretNotFoundError:
        return os.getenv("OPENAI_API_KEY")


st.set_page_config(page_title="Concise AI Q&A", page_icon="💬")
st.title("Concise AI Q&A")
st.write("Ask a question and get a concise answer powered by OpenAI.")

api_key = get_api_key()
if not api_key:
    st.info(
        "Set `OPENAI_API_KEY` in Streamlit secrets or as an environment variable "
        "to enable answers."
    )

with st.form("question_form"):
    question = st.text_area("Your question", placeholder="What is the tallest mountain?")
    submitted = st.form_submit_button("Get answer", type="primary")

if submitted:
    question = question.strip()
    if not question:
        st.warning("Enter a question to continue.")
    elif not api_key:
        st.error("OpenAI API key is not configured.")
    else:
        prompt = ChatPromptTemplate.from_template(
            "Answer the following question concisely: {question}"
        )
        chain = prompt | ChatOpenAI(
            model="gpt-4",
            api_key=api_key,
            temperature=0.7,
        ) | StrOutputParser()

        with st.spinner("Generating an answer..."):
            try:
                st.session_state["answer"] = chain.invoke({"question": question})
                st.session_state["question"] = question
            except OpenAIError as exc:
                st.error(f"OpenAI request failed: {exc}")

if "answer" in st.session_state:
    st.subheader("Answer")
    st.markdown(st.session_state["answer"])
