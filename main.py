from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import run_orchestrator
from memory_agent import retrieve_memory

# ---- CREATE APP FIRST ----
app = FastAPI(
    title="Multi-Agent AI Task System 🚀",
    description="AI-powered system using Planner, Task, Scheduler, and Memory agents",
    version="1.0"
)

# ---- REQUEST MODEL ----
class GoalRequest(BaseModel):
    goal: str

# ---- RUN ENDPOINT ----
@app.post("/run")
def run(request: GoalRequest):
    print("RUN ENDPOINT CALLED")
    return run_orchestrator(request.goal)

# ---- MEMORY ENDPOINT ----
@app.get("/memory")
def get_memory():
    return retrieve_memory()

# ---- HOME ENDPOINT ----
@app.get("/")
def home():
    return {"message": "Multi-Agent AI System is running 🚀"}