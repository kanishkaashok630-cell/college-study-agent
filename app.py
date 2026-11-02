import streamlit as st
from google import genai

st.set_page_config(page_title="College Study Agent")
st.title("📚 College Study Assistant")

topic = st.text_input("Enter a subject or topic",
                      placeholder="Example: Cloud Computing")
task = st.selectbox("What do you need?",
    ["Simple explanation", "Quiz questions", "Both"])

if st.button("Help me learn"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        try:
            client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
            prompt = f"""
You are a friendly college study assistant.
Topic: {topic}
Student request: {task}

Explain in simple student-friendly language.
If a quiz is requested, create 3 practice questions
and provide answers separately.
"""
            with st.spinner("Preparing your study help..."):
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
