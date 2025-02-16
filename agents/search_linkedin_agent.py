from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

from tools.linkedin_url_search_tool import get_linkedin_url_search_tavily


def lookup(name: str):
    """llm = ChatOllama(model="deepseek-r1:8b")"""
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
    )

    template = """Given the full name {name_of_person}, return only the most relevant LinkedIn profile URL.
Your answer should contain only the URL and nothing else."""
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    tools = [
        Tool(
            name="Crawl Google 4 LinkedIn profile page",
            func=get_linkedin_url_search_tavily,
            description="useful for when you need to get the Linkedin profile Page URL.",
        )
    ]

    prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    executor = AgentExecutor(
        agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
    )

    res = executor.invoke(
        input={
            "input": prompt_template.format_prompt(name_of_person=name),
        }
    )
    linkedin_profile_url = res["output"]

    return linkedin_profile_url
