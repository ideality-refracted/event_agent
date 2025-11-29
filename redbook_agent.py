from google.adk.agents.llm_agent import Agent
from .utils import read_markdown_file_as_string


# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}


redbook_agent = Agent(
    model='gemini-2.5-pro',
    name='redbook_agent',
    description="Tells the current time in a specified city.",
    instruction=read_markdown_file_as_string("redbook_instruction.md"),
    tools=[get_current_time],
)