
from src.dsa_agent.teams.dsa_solver_team import get_dsa_solver_team
from src.dsa_agent.utils.docker_utils import get_docker_executor, start_docker_executor, stop_docker_executor
from src.dsa_agent.model_clients.openai_model_client import get_model_client
from src.dsa_agent.agents.code_executor_agent import get_code_executor_agent
from src.dsa_agent.agents.problem_solver_agent import get_problem_solver_agent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def get_team_and_docker():
    
    model_client = get_model_client()
    problem_solver_agent = get_problem_solver_agent(model_client)
    
    docker_executor = get_docker_executor()
    code_executor_agent = get_code_executor_agent(docker_executor)
    
    dsa_solver_team = get_dsa_solver_team(problem_solver_agent, code_executor_agent)
    
    return dsa_solver_team, docker_executor

async def run_team(task):
   
    try:
        
        team,docker = await get_team_and_docker()
        task = task

        await start_docker_executor(docker)

        async for message in team.run_stream(task = task):
            print('='*50)
            if isinstance(message, TextMessage):
                print(msg:= f" {message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:=f'Task Result: {message.stop_reason}')
                yield msg
            print('='*50)


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        await stop_docker_executor(docker)