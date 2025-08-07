# app/utils/llm_config.py

from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

# Returns an OpenAI Chat model instance (e.g., gpt-4 or gpt-3.5-turbo)
def get_openai_llm(model="gpt-4"):
    return ChatOpenAI(
        model=model,
        temperature=0.3,
        openai_api_key=OPENAI_API_KEY
    )
