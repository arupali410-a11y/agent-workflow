from tools import calculator_tool, chat_tool, time_tool
from memory import add_memory, search_memory


def agent(query):

    user_id = "rupali"

    query_lower = query.lower()

    # Calculator
    if all(char in "0123456789+-*/(). " for char in query):
        answer = calculator_tool(query)

    # Time & Date
    elif "time" in query_lower or "date" in query_lower:
        answer = time_tool()

    # AI
    else:

        previous_memory = search_memory(user_id)

        prompt = f"""
You are a helpful AI assistant.

Here is the previous conversation with the user.

{previous_memory}

Current User:
{query}

Answer naturally while remembering previous conversations.
"""

        answer = chat_tool(prompt)

    add_memory(user_id, query, answer)

    return answer