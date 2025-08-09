import streamlit as st
import requests

st.set_page_config("Langgraph AI Agent", layout="centered")


st.title("Langgraph AI Agent")
st.write("Create and Interact with Ai Agents")

system_prompt = st.text_area("Define Role of Agent",height=70 ,placeholder="Write system prompt here")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]
MODEL_NAMES_GOOGLE = ["gemini-2.5-flash"]

provider = st.radio("Select Provider: ",("Google", "Groq"))
if provider == "Google":
    selected_id = st.selectbox("Select Google Models:", MODEL_NAMES_GOOGLE)
elif provider == "Groq":
    selected_id = st.selectbox("Select Groq Models:",MODEL_NAMES_GROQ)

allow_web_search = st.checkbox("Allow Web Search")

query = st.text_area("query:", height=150, placeholder="Ask Anything")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask"):
    if query.strip():

        payload = {
        "model_name" : selected_id,
        "provider" :provider,
        "prompt" : system_prompt,
        "query" : [query],
        "allow_search" : allow_web_search
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:        
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")
            

           
