from fastapi import FastAPI
from app.schemas.request import CareerQuery
from app.agent.career_agent import run_career_agent

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Career Agent is running"}

@app.post("/suggest")
def suggest_career(query: CareerQuery):
    result = run_career_agent(query.interests)
    return result
