import streamlit as st
from agent import agent

st.title("🤖 Simple AI Agent")

query = st.text_input("Ask anything")

if st.button("Ask"):

    if query:

        with st.spinner("Thinking..."):

            answer = agent(query)

        st.write("### Answer")
        st.write(answer)