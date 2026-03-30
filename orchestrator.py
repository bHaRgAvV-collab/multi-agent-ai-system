

from planner_agent import planner_agent
from task_agent import task_agent
from scheduler_agent import scheduler_agent
from memory_agent import store_memory
import json
import os

print("🔥 THIS ORCHESTRATOR FILE IS RUNNING 🔥")

def run_orchestrator(user_query):
    print("👉 Inside run_orchestrator")

    goal = user_query

    # Step 1: Planner
    plan = planner_agent(goal)
    print("PLAN:", plan)

    # Step 2: Task Agent
    tasks = task_agent(plan)
    print("TASKS:", tasks)

    # Step 3: Scheduler Agent
    schedule = scheduler_agent(tasks)
    print("SCHEDULE:", schedule)

    # Step 4: Save final schedule to JSON
    file_path = os.path.join(os.path.dirname(__file__), "task_db.json")

    with open(file_path, "w") as f:
        json.dump(schedule, f, indent=4)

    # Step 5: Store in memory
    store_memory(goal, schedule)

    # Final structured response
    result = {
        "goal": goal,
        "steps": [
            {
                "agent": "Planner",
                "action": "Generate plan",
                "output": plan
            },
            {
                "agent": "Task",
                "action": "Convert plan to tasks",
                "output": tasks
            },
            {
                "agent": "Scheduler",
                "action": "Assign time slots",
                "output": schedule
            },
            {
                "agent": "Memory",
                "action": "Store workflow",
                "output": "Saved successfully"
            }
        ],
        "final_response": "Multi-agent workflow executed successfully 🚀"
    }

    print("RETURNING FULL RESULT")
    return result