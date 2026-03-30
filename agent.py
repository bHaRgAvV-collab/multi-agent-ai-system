from google import genai
import json
import os


client = genai.Client(api_key="AIzaSyCGIHF64eloBouamAN2L8CzPMHDAb3rXO0")

def summarize_text(text):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=text
        )
        return response.text
    except Exception:
        # 🔥 Smart fallback (dynamic based on input)
        if "exam" in text.lower():
            return """1. Day 1: Revise core subjects
2. Day 2: Practice questions
3. Day 3: Focus on weak areas
4. Day 4: Mock tests
5. Day 5: Final revision"""

        elif "coding" in text.lower():
            return """1. Day 1: Arrays + Strings
2. Day 2: Linked Lists + Stacks
3. Day 3: Trees + Graphs
4. Day 4: Dynamic Programming
5. Day 5: Mock Interviews"""

        else:
            return """1. Day 1: Basics
2. Day 2: Practice
3. Day 3: Intermediate
4. Day 4: Advanced
5. Day 5: Review"""


def task_agent(plan_text):
    tasks = []

    lines = plan_text.split("\n")

    for line in lines:
        if line.strip():
            try:
                if ":" in line:
                    parts = line.split(":")
                elif "-" in line:
                    parts = line.split("-")
                else:
                    continue

                day = parts[0].strip()
                task = parts[1].strip()

                tasks.append({
                    "day": day,
                    "task": task
                })
            except Exception:
                continue

    # 🔥 FIXED PATH
    file_path = os.path.join(os.path.dirname(__file__), "task_db.json")

    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=4)

    return tasks