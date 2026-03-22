import streamlit as st
import requests

st.title("AI STEM Tutor")

st.write("Ask any question (STEM or general):")

# Use session_state to preserve input
if "question" not in st.session_state:
    st.session_state["question"] = ""

def submit():
    st.session_state["question"] = st.session_state["input_question"]

question = st.text_input(
    "Your question",
    value=st.session_state["question"],
    key="input_question",
    on_change=submit
)

agent = st.selectbox(
    "Choose agent (or leave as Auto):",
    ["Auto (Detect)", "General", "Math", "Retrieve"]
)

if st.button("Ask"):
    # Decide endpoint based on agent
    endpoint = "http://localhost:8001/ask"
    payload = {"user_id": "streamlit_user", "question": question}
    if agent == "Math":
        endpoint = "http://localhost:8001/solve"
        payload = {"user_id": "streamlit_user", "problem": question}
    elif agent == "Retrieve":
        endpoint = "http://localhost:8001/retrieve"
        payload = {"user_id": "streamlit_user", "query": question, "top_k": 3}
    # General and Auto both use /ask

    try:
        response = requests.post(endpoint, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        st.subheader("Answer:")
        st.write(data.get("answer") or data.get("message"))
        if data.get("steps"):
            st.markdown("**Steps:**")
            for step in data["steps"]:
                st.write("-", step)
        if data.get("sources"):
            st.markdown("**Sources:**")
            for src in data["sources"]:
                st.write(src)
    except Exception as e:
        st.error(f"Error: {e}")

# Temporarily disabled speech functionality
# if st.button("Speak It"):
#     response = requests.post("http://localhost:8001/speak", json={"text": question})
#     audio_path = response.json()["file_path"]
#     with open(audio_path, "rb") as f:
#         st.audio(f.read(), format="audio/wav")
