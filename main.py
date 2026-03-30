from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import run_orchestrator
from memory_agent import retrieve_memory

app = FastAPI(
    title="Multi-Agent AI Task System 🚀",
    description="AI-powered system using Planner, Task, Scheduler, and Memory agents",
    version="1.0"
)

class UserRequest(BaseModel):
    query: str


@app.post("/run")
def run(req: UserRequest):
    print("RUN ENDPOINT CALLED")
    return run_orchestrator(req.query)


@app.get("/memory")
def get_memory():
    return retrieve_memory()


@app.get("/")
def home():
    return {"message": "Multi-Agent AI System is running 🚀"}