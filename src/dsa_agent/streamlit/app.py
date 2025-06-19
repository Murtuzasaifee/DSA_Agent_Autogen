import streamlit as st
import asyncio
from src.dsa_agent.teams.team_executor import run_team

async def load_app():
    
    st.title("DSA Solver")
    st.write("This is a simple DSA solver application.")

    task = st.text_input("Enter your DSA Question here",value='Can you give me a solution to add 2 numbers?')



    if st.button("Solve"):
        st.write('Solving your question...')

        
        task = task

        async for msg in run_team(task):
            print("Message:",msg)
            if msg.startswith(' user'):
                with st.chat_message('User',avatar='👤'):
                    st.markdown(msg)
            elif msg.startswith(' ProblemSolverExpert'):
                with st.chat_message('ProblemSolverExpert',avatar='🧑🏻‍💻') :
                    st.markdown(msg)
            elif msg.startswith(' CodeExecutorAgent'):
                with st.chat_message('CodeExecutorAgent',avatar='🤖'):
                    st.markdown(msg)
            else:
                st.markdown(msg)
