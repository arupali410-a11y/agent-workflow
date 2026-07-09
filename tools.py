from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def chat_tool(prompt):
    response = llm.invoke(prompt)
    return response.content
def calculator_tool(query):
    try:
        return str(eval(query))
    except:
        return "Invalid math expression"