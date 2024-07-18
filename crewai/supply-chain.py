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


@tool("get_data")
def get_data():
    """
    Fetches dummy historical sales data, market trends, and external factors for demand forecasting.

    Returns:
        dict: A dictionary containing dummy data for items, market trends, and external factors.
    """

    # Dummy historical sales data
    data = {
        "items": [
            {"item_id": 1, "name": "Product A", "historical_sales": [120, 135, 150, 145, 160]},
            {"item_id": 2, "name": "Product B", "historical_sales": [80, 90, 95, 100, 105]},
            {"item_id": 3, "name": "Product C", "historical_sales": [200, 210, 220, 215, 230]},
            {"item_id": 4, "name": "Product D", "historical_sales": [60, 70, 65, 75, 80]},
            {"item_id": 5, "name": "Product E", "historical_sales": [140, 150, 160, 155, 165]},
        ],
        "market_trends": [
            {"month": "January", "trend": "steady"},
            {"month": "February", "trend": "increase"},
            {"month": "March", "trend": "increase"},
            {"month": "April", "trend": "steady"},
            {"month": "May", "trend": "increase"},
        ],
        "external_factors": [
            {"factor": "seasonality", "impact": "high"},
            {"factor": "promotions", "impact": "medium"},
            {"factor": "economic_conditions", "impact": "low"},
        ]
    }
    return data


demand_forecaster = Agent(
  role='Supply Chain Demand Forecaster',
  goal='Accurately forecast demand for {input} in the supply chain',
  backstory="""You work at a leading logistics company.
  Your expertise lies in demand forecasting, inventory management, and supply chain optimization.
  You utilize advanced statistical models and machine learning algorithms to predict future demand and optimize stock levels.""",
  verbose=True,
  allow_delegation=False,
  llm = GROQ_LLM,
)


task1 = Task(
  description="""Analyze historical sales data and market trends to forecast demand for {input} in the supply chain.""",
  expected_output="A detailed report including demand forecasts, identified trends, and recommendations for inventory management in comprehensive paragraphs.",
  agent=demand_forecaster,
  tools=[get_data]
)


def print_agent_output(step_output, crew_name):
    print(f"{crew_name} step output: {step_output}")

crew = Crew(
    agents=[demand_forecaster],
    tasks=[task1],
    verbose=2,
    step_callback=lambda x: print_agent_output(x, "Crew")
)

result = crew.kickoff(inputs={"input": "Product B"})
print(result)



