import json
import os

def task_agent(plan_text):
    tasks = []

    for line in plan_text.split("\n"):
        if line.strip():
            try:
                if ":" in line:
                    parts = line.split(":")
                elif "-" in line:
                    parts = line.split("-")
                else:
                    continue

                day = parts[0].strip()

                if "." in day:
                    day = day.split(".", 1)[1].strip()

                task_text = parts[1].strip()

                tasks.append({
                    "day": day,
                    "task": task_text
                })

            except Exception:
                continue

    file_path = os.path.join(os.path.dirname(__file__), "task_db.json")

    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=4)

    return tasks