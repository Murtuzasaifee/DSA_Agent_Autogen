from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from src.dsa_agent.configs.constants import TEXT_MENTION_TERMINATION, MAX_TURNS  




def get_dsa_solver_team(problem_solver_expert, code_executor_agent):
    
    termination_condition = TextMentionTermination(TEXT_MENTION_TERMINATION)
    
    team = RoundRobinGroupChat(
        participants=[problem_solver_expert, code_executor_agent],
        termination_condition=termination_condition,
        max_turns=MAX_TURNS,
    )
    
    return team
