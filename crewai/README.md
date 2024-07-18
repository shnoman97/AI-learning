# Supply Chain Demand Forecaster

This project is a supply chain demand forecasting system built using the CrewAI and LangChain libraries. It utilizes a fictional `ChatGroq` model for generating demand forecasts based on historical sales data, market trends, and external factors.

## Installation

1. Clone the repository:

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required packages:

    ```sh
    pip install langchain-groq crewai langchain_community
    ```

3. Set up the environment variable for the Groq API key:

    ```sh
    export GROQ_API_KEY=<your_groq_api_key>
    ```

    To generate an API key, visit [console.groq.com](https://console.groq.com).

## Usage

The main components of the project are:

1. **Agents**: Represent different roles in the supply chain process. In this example, we have a `demand_forecaster` agent.
2. **Tasks**: Define specific tasks that agents need to perform. Here, we have a task to analyze historical sales data and forecast demand.
3. **Tools**: Utilities or functions that agents use to gather data or perform specific actions. The `get_data` tool fetches dummy historical sales data, market trends, and external factors.

### Running the Forecaster

To run the demand forecaster, execute the main script:

```sh
python supply-chain.py
