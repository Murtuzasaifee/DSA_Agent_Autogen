from autogen_agentchat.messages import TextMessage
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.base import TaskResult



def get_dsa_solver_team(problem_solver_expert, code_executor_agent):
    
    termination_condition = TextMentionTermination('STOP')
    
    team = RoundRobinGroupChat(
    participants=[problem_solver_expert, code_executor_agent],
    termination_condition=termination_condition,
    max_turns=15)
    
    return team
