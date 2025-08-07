# app/agent/career_agent.py

from langchain_core.runnables import RunnableSequence
from app.chains.interest_chain import get_interest_chain
from app.chains.skill_chain import get_skill_chain
from app.chains.resource_chain import get_resource_chain

# Build the final sequence
# Step 1: Interest ➜ Careers
# Step 2: Careers ➜ Skills
# Step 3: Careers ➜ Resources

# Initialize chains
interest_chain = get_interest_chain()
skill_chain = get_skill_chain()
resource_chain = get_resource_chain()

def run_career_agent(interests: str) -> dict:
    # Step 1: Get career suggestions
    careers_text = interest_chain.invoke({"interests": interests}).content.strip()

    # Step 2: Get skill and salary info
    skills_text = skill_chain.invoke({"careers": careers_text}).content.strip()

    # Step 3: Get resource links
    resources_text = resource_chain.invoke({"careers": careers_text}).content.strip()

    return {
        "careers": careers_text,
        "skills_and_salary": skills_text,
        "resources": resources_text
    }
