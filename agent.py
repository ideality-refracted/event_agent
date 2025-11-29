from google.adk.agents.llm_agent import Agent
from .eventbrite_agent import eventbrite_agent
from .redbook_agent import redbook_agent
from .utils import read_markdown_file_as_string


root_agent = Agent(
    model='gemini-2.5-pro',
    name='root_agent',
    description="The root agent.",
    instruction=read_markdown_file_as_string("root_agent.md"),
    sub_agents = [eventbrite_agent, redbook_agent],
)