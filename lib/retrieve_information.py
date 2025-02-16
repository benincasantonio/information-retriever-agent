from lib import linkedin
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from agents.search_linkedin_agent import lookup
from validators import url as is_url_valid
from typing import Tuple

from parsers.summary_parser import summary_parser, Summary


def retrieve_information(name: str, mock: bool = False) -> Tuple[Summary, str]:
    template = """
Given the LinkedIn information {information} about a person I want you to give me:

    1. A short description of the person
    2. Some interesting facts about them

    Use information from LinkedIn:
    \n{format_instructions}"""

    prompt_template = PromptTemplate(
        input_variables=["information"],
        template=template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOllama(model="phi4")

    # llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    chain = prompt_template | llm | summary_parser

    linkedin_profile_url = lookup(name)

    if (
        not linkedin_profile_url
        or linkedin_profile_url == ""
        or not is_url_valid(linkedin_profile_url)
    ):
        raise ValueError("LinkedIn profile not found")

    linkedin_data = linkedin.scrape_linkedin_profile(linkedin_profile_url, mock=mock)

    response: Summary = chain.invoke(input={"information": linkedin_data})
    return response, linkedin_data['photoUrl']

