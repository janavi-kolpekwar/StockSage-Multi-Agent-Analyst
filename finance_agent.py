from phi.agent import Agent, RunResponse
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import openai
import os
from dotenv import load_dotenv


load_dotenv()

def get_company_symbol(company: str) -> str:
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft":"MSFT",
        "Amazon":"AMZN",
        "Google":"GOOGL",
    }
    return symbols.get(company, "Unknown")


agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile"),
    model =OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Use tables to display data.",
        "If you don't know the company symbol, please use get_company_symbol tool, even if it is not a public company"],
    debug_mode=True,
)
