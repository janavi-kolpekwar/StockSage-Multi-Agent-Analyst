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

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)


finance_agent = Agent(
    name = "Finance Agent",
    role="Recieve financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data"],
    debug_mode=True,
)

agent_team = Agent(
    team=[web_agent,finance_agent],
    model =OpenAIChat(id="gpt-4o"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)


agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)