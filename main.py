import asyncio
from src.dsa_agent.teams.team_executor import run_team
from src.dsa_agent.streamlit.app import load_app


async def main():
    ## Run team via CLI
    # task = 'Write a Python Code to add 2 numbers'
    # await run_team(task)
    
    ## Run team via Streamlit
    await load_app()
    
    


if __name__ == "__main__":
    # Run the main function using asyncio
    asyncio.run(main())