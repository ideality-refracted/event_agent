from google.adk.agents.llm_agent import Agent
from .redbook_agent import redbook_agent


root_agent = Agent(
    model='gemini-2.5-pro',
    name='root_agent',
    description="The root agent.",
    instruction=read_markdown_file_as_string("root_agent.md"),
    sub_agents = [redbook_agent],
)