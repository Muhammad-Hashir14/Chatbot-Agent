# Langgraph AI Agent

Create and interact with an AI agent that has search capabilities using two major AI model providers: Groq and Google.

## How to Run

### 1- Clone Respository
```bash
git clone https://github.com/Muhammad-Hashir14/Chatbot-Agent.git
```
### 2- Create Virtual Enviornment
```bash 
pip install virtualenv
virtualenv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For macOS/Linux
```

### 3. Install Dependencies
```bash 
pip install -r requirements.txt
```

### 4. Create a .env File
```bash 
GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TAVILY_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 5. Run the Server App
```bash
python main.py
```

### 5. Run the Streamlit App
```bash
python app.py
```

### 💻 Tech Stack Used
- Python
- Streamlit
- Langgraph
- Gemini (Google LLM)
- Groq 
- Tavily
- FastAPI

___
🙋‍♂️ Author:

- Developed by Muhammad Hashir

