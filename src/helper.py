import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
import dotenv

load_dotenv()
from langchain_core.messages.ai import AIMessage

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

def getresponse(llm_id, provider, prompt, query, allow_search):
    # Initialize the LLM based on provider
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    else:
        llm = ChatGoogleGenerativeAI(model=llm_id)

    # Add search tool only if allowed
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Create the ReAct agent
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=prompt
    )

    # Invoke agent with message state
    state = {"messages": query}
    result = agent.invoke(state)

    # Extract the AI message(s)
    if isinstance(result, dict) and "messages" in result:
        messages = result["messages"]
        ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]
        return ai_messages[-1] if ai_messages else None
    elif isinstance(result, AIMessage):
        return result.content
    else:
        return str(result)  # fallback in case of unexpected return format