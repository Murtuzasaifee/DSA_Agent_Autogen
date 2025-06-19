import asyncio
from src.dsa_agent.teams.team_executor import run_team


async def main():
    task = 'Write a Python Code to add 2 numbers'

    await run_team(task)
    


if __name__ == "__main__":
    # Run the main function using asyncio
    asyncio.run(main())