from crewai import Agent, Task, LLM
import os
from dotenv import load_dotenv
from crewai import Crew, Process
from crewai_tools import SerperDevTool

load_dotenv()

# Note: Remove the trailing comma after the tuple
default_llm = LLM(
    model="openai/meta-llama/Meta-Llama-3.1-70B-Instruct",
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY")
)

# Create a researcher agent
researcher = Agent(
    role="Senior Researcher",
    goal="Uncover AI trends in healthcare",
    backstory="You are an expert in AI research.",
    tools=[SerperDevTool()],
    llm=default_llm  # Added LLM for consistency
)

# Create a writer agent
writer = Agent(
    role="Content Writer",
    goal="Write a compelling article on AI in healthcare.",
    verbose=True,
    llm=LLM(
        model="openai/meta-llama/Meta-Llama-3.1-70B-Instruct",
        base_url="https://api.studio.nebius.com/v1/",
        api_key=os.getenv("NEBIUS_API_KEY")
    ),
    backstory="You excel at translating complex topics into readable content.",
    tools=[]
)

# Tasks with agent assignments
research_task = Task(
    description="Research the latest AI trends in healthcare.",
    expected_output="A report summarizing key trends.",
    agent=researcher  # Assign the researcher agent
)

write_task = Task(
    description="Write a 3-paragraph article based on the research.",
    expected_output="An engaging article on AI in healthcare.",
    agent=writer,  # Assign the writer agent
    context=[research_task]  # Use research task output as context
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential  # The agents work in sequence
)

# Execute the crew and capture the result
result = crew.kickoff(inputs={"topic": "AI in healthcare"})
print(result)