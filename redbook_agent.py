from google.adk.agents.llm_agent import Agent
from .utils import read_markdown_file_as_string
from .inference_tool import genai_model_inference


redbook_agent = Agent(
    model='gemini-2.5-pro',
    name='redbook_agent',
    description="Tells the current time in a specified city.",
    instruction=read_markdown_file_as_string("redbook_instruction.md"),
    tools=[genai_model_inference],
)