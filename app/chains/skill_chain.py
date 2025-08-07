# app/chains/skill_chain.py

from langchain_core.prompts import ChatPromptTemplate
from app.utils.llm_config import get_openai_llm

llm = get_openai_llm()

prompt = ChatPromptTemplate.from_template(
    """
    For each of these careers:
    {careers}

    List the top 3 skills required and expected salary range in INR.
    Keep it short and structured.
    """
)

def get_skill_chain():
    return prompt | llm
