from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

load_dotenv(override=True)

llm = LLM(model="gemini/gemini-2.0-flash-exp", temperature=0.5, api_key=os.environ.get("GOOGLE_API_KEY"))

researcher = Agent(
    role= "{topic} Senior Researcher",
    goal="""
        Uncover groundbreaking technologies in {topic} for year 2024
    """,
    backstory="Driven by curiosity, you  explore and share the latest innovations.",
    tools=[SerperDevTool()],
    llm=llm
)

task= Task(
    description="Identify the next big trend in {topic} with pros and cons.",
    expected_output="A 3-paragraph report on emerging {topic} technologies.",
    agent=researcher
)

def main():
    crew = Crew(
        agents=[researcher],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": "AI agents"})

    print(result)

if __name__ == "__main__":
    main()