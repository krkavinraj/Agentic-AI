import os
from dotenv import load_dotenv

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app


load_dotenv()

websearch_agent = Agent(
    name="websearch_agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include the source of the information in the response"],
    show_tools_called=True,
    markdown=True,
)

financial_agent = Agent(
    name="Financial AI Agent",
    role="Get financial data",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use Tables To Display the data"],
    show_tools_called=True,
    markdown=True,
)

app = Playground(
    agents=[websearch_agent, financial_agent]
).get_app()


if __name__=="__main__":
    serve_playground_app("playground:app",reload=False)