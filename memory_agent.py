import json
import os

def store_memory(goal, schedule):
    file_path = os.path.join(os.path.dirname(__file__), "memory.json")

    data = {
        "goal": goal,
        "schedule": schedule
    }

    # Load existing memory
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            memory = json.load(f)
    else:
        memory = []

    memory.append(data)

    with open(file_path, "w") as f:
        json.dump(memory, f, indent=4)


def retrieve_memory():
    file_path = os.path.join(os.path.dirname(__file__), "memory.json")

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        return json.load(f)