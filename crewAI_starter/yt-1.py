from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os
from crewai import Process, Crew
load_dotenv()

llm =LLM(
    model = "openai/meta-llama/Meta-Llama-3.1-70B-Instruct",
    base_url = "https://api.studio.nebius.com/v1/",
    api_key = os.getenv("NEBIUS_API_KEY"),
)

agent = Agent(
    role="senior software engineer",
    goal="Discover groundbreaking technologies in quantum computing",
    verbose=True,
    llm=llm,
    backstory="A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about quantum computing and its applications."
)

task = Task(
    description="Research and summarize the latest advancements in quantum computing, focusing on practical applications and future potential.",
    expected_output="A comprehensive report detailing the latest advancements in quantum computing, including practical applications and future potential, with references to key research papers and articles.",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential
)

crew.kickoff()
