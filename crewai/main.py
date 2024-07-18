import os

from langchain_groq import ChatGroq

from crewai import Crew, Agent, Task, Process
from langchain_community.tools import DuckDuckGoSearchRun

from langchain.tools import tool

from crewai_tools import tool


GROQ_LLM = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192"
        )



@tool('DuckDuckGoSearch')
def search(search_query: str):
    """Search the web for information on a given topic"""
    return DuckDuckGoSearchRun().run(search_query)


researcher = Agent(
  role='Senior Research Analyst',
  goal='what are the latest News',
  backstory="""You work at a leading think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  llm = GROQ_LLM,
  tools=[
        search
      ],

)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on recent advancements',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=False,
  llm = GROQ_LLM,
)

task1 = Task(
  description="""Conduct News search and find the latest about Arizona State University.""",
  expected_output="Full analysis report in comprehensive paragraphs",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog
  post that highlights latest AI related progresses in Arizona State University.""",
  expected_output="Full blog post of at least 4 paragraphs",
  agent=writer
)

def print_agent_output(step_output, crew_name):
    print(f"{crew_name} step output: {step_output}")

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    step_callback=lambda x: print_agent_output(x, "Crew")
)

result = crew.kickoff()
print(result)