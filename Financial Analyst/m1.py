import os
import agentops
from embedchain import App

from crewai import Agent, Task, Crew
from textwrap import dedent

from crewai_tools import PDFSearchTool, SerperDevTool, ScrapeWebsiteTool, tool
from langchain_groq import ChatGroq
from llama_parse import LlamaParse

os.environ["GROQ_API_KEY"] = "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"
os.environ["SERPER_API_KEY"] = "1bc2e37176d18d5ea86e75c5394237e450a5955c"
os.environ["AGENTOPS_LOGGING_LEVEL"] = "WARNING"
# agentops.init(api_key="61105c50-1b53-47a2-a414-de040e361848", tags=["financial_analyst_crew"])
agentops.init(api_key="0e86b61c-d67b-4c7d-9fa5-42debd67b145", tags=["financial_analyst_crew"])

GROQ_LLM = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192"
        )

def tip_section():
    return "If you do your BEST WORK, I'll give you a $10,000 commision!"

# def load_or_parse_data():
#     data_dir = "./data"
#     data_file = os.path.join(data_dir, "new-parsed-data.md")

#     if not os.path.exists(data_dir):
#         os.makedirs(data_dir)

#     if os.path.exists(data_file):
#         # Load the parsed data from the file
#         parsed_data = joblib.load(data_file)
#     else:
#         # Perform the parsing step and store the result in llama_parse_documents
#         parsing_instruction_uber10k = """The provided document is a quarterly report filed by ATTOCK CEMENT PAKISTAN LIMITED
#         with the Securities and Exchange Commission Pakistan (SECP).
#         This form provides detailed financial information about the company's performance for a specific quarter.
#         It includes unaudited financial statements, management discussion and analysis, and other relevant disclosures required by the SECP.
#         It contains many tables.
#         Try to be precise while answering the questions"""
        
#         parser = LlamaParse(api_key="llx-6S0lXWfj4wZMjlk72KpK6MZEDXDICvGFxunss41q8yrcziI2",
#                             result_type="markdown",
#                             parsing_instruction=parsing_instruction_uber10k,
#                             max_timeout=5000)
#         llama_parse_documents = parser.load_data("./files/230965.pdf")

#         # Save the parsed data to a file
#         print("Saving the parse results in .pkl format ..........")
#         joblib.dump(llama_parse_documents, data_file)

#         # Set the parsed data to the variable
#         parsed_data = llama_parse_documents

#     return parsed_data


# llama_parse_documents = load_or_parse_data()

# print("llama_parse_documents : ", llama_parse_documents)
# with open('data/output.md', 'a') as f:  # Open the file in append mode ('a')
#         for doc in llama_parse_documents:
#             f.write(doc.text + '\n')

config = {
  'llm': {
    'provider': 'groq',
    'config': {
      'model': 'llama3-70b-8192',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'ollama',
    'config': {
      'model': 'all-minilm'
    }
  }
}

app = App.from_config(config=config)
app.add("./data/output.md")


@tool
def search_from_doc(inp: str):
    """Use this function to search from markdown file of a company's quarterly report."""
    return app.query(inp)


pdf_tool = PDFSearchTool(
    pdf="./files/230965.pdf",
    config=dict(
        llm=dict(
            provider="groq", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama3-70b-8192",
                temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="ollama", # or openai, ollama, ...
            config=dict(
                model="all-minilm",
                # task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)



financial_analyst = Agent(
      role='The Best Financial Analyst of Pakistan Stocks Exchange',
      goal="""Impress all customer with your financial data 
      and market trends analysis of Pakistan Stocks Exchange""",
      backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
      llm = GROQ_LLM,
      allow_delegation = False,
      tools=[search_from_doc, ScrapeWebsiteTool(), SerperDevTool()],
      verbose=True
    )

financial_analysis = Task(
    description=dedent(f"""
        Conduct a thorough analysis of the {{c_name}} financial
        health and market performance on the file. 
        This includes examining key financial metrics such as
        P/E ratio, EPS growth, revenue trends, and 
        debt-to-equity ratio. 
        Also, analyze the stock's performance in comparison 
        to its industry peers and overall market trends.
        Search from internet if information not available in file.

        Your final report MUST expand on the summary provided
        but now including a clear assessment of the stock's
        financial standing, its strengths and weaknesses, 
        and how it fares against its competitors in the current
        market scenario.{tip_section()}

        Make sure to use the most recent data as possible.
    """),
    agent=financial_analyst,
    output_file='outputs/report.txt',
    create_directory=True,
    expected_output="A detailed financial analysis report with assessments of the stock's financial standing, strengths and weaknesses, and comparisons with industry peers and market trends."
)


crew = Crew(
      agents=[
        financial_analyst        
      ],
      tasks=[
        financial_analysis,
      ],
      verbose=2,
      cache=True
    )

result = crew.kickoff(inputs={"c_name": "ACPL"})
print(result)

