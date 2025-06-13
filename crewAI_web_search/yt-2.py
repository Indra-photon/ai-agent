import os
from dotenv import load_dotenv
from crewai import  Crew, Process, LLM, Agent, Task
from crewai_tools import YoutubeVideoSearchTool, YoutubeVideoSearchTool

load_dotenv()
llm = LLM(
    model = "openai/meta-llama/Meta-Llama-3.1-70B-Instruct",
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY")
)

researcher = Agent (
    role="youtube video details e.g. tiltle, description, tags, channel analysis",
    goal="Uncover the hidden tags, title, description, and channel analysis of YouTube videos in a specific niche.",    
    backstory="You are an expert in YouTube video analysis, specializing in extracting detailed metadata and insights from videos.",
    tools=[YoutubeVideoSearchTool(), YoutubeVideoSearchTool()],
    llm=llm
)

writer = Agent(
    role="Report Writer",
    goal="Write a compelling report on the YouTube video analysis findings focusing on numbers views tags title, description, and channel " \
    "analysis. Try to find the most popular videos in the niche and its success factors. write in a professional tone, to the point, "
    "and with a focus on actionable insights. Use bullet points for clarity. focus on numbers.",
    verbose=True,
    llm=llm,
    backstory="You excel at translating complex data into readable content, focusing on actionable insights and clarity.",
)

research_task = Task(
    description="Research the successful YouTube videos in the niche of AI agents, focusing on their tags, titles, descriptions, and channel analysis.",
    expected_output="A report summarizing key insights from the YouTube videos, including tags, titles, descriptions, and channel analysis.",
    agent=researcher  # Assign the researcher agent
)

write_task = Task(
    description="Write a detailed report based on the YouTube video analysis findings, focusing on numbers views tags title, description, and channel analysis.",
    expected_output="An engaging report on the YouTube video analysis findings, highlighting key metrics and insights.",
    agent=writer,  # Assign the writer agent
    context=[research_task]  # Use research task output as context
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

crew.kickoff()