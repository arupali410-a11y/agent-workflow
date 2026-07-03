from tools import chat_tool

def agent(query):

    prompt = f"""
You are an AI assistant.

Your job is to answer the user's question clearly.

Question:
{query}

Answer:
"""

    answer = chat_tool(prompt)

    return answer