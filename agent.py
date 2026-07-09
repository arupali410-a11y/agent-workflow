from tools import calculator_tool, chat_tool

def agent(query):

    # If the query contains only numbers and math operators
    if all(char in "0123456789+-*/(). " for char in query):
        return calculator_tool(query)

    # Otherwise use the AI
    return chat_tool(query)