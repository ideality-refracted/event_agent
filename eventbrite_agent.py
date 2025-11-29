from google.adk.agents.llm_agent import Agent
from .utils import read_markdown_file_as_string


eventbrite_agent = Agent(
    model='gemini-2.5-pro',
    name='eventbrite_agent',
    description="Hello world.",
    instruction=read_markdown_file_as_string("eventbrite_agent.md"),
)