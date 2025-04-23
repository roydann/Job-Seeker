import os
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import OpenAI
from langchain_community.utilities import SerpAPIWrapper


os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")

llm = OpenAI(temperature = 0)

search = SerpAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for searching job listing from the web."
    )
]

job_agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)