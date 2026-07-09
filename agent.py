from tools import calculator_tool, chat_tool, time_tool


def agent(query):

    query_lower = query.lower()

    # Calculator
    if all(char in "0123456789+-*/(). " for char in query):
        return calculator_tool(query)

    # Time tool
    elif "time" in query_lower or "date" in query_lower:
        return time_tool()

    # Otherwise use AI
    else:
        return chat_tool(query)