def planner_agent(goal):
    if "coding" in goal.lower():
        return """1. Day 1: Arrays + Strings
2. Day 2: Linked Lists + Stacks
3. Day 3: Trees + Graphs
4. Day 4: Dynamic Programming
5. Day 5: Mock Interviews"""

    elif "exam" in goal.lower():
        return """1. Day 1: Revise core subjects
2. Day 2: Practice questions
3. Day 3: Weak areas
4. Day 4: Mock test
5. Day 5: Revision"""

    else:
        return """1. Day 1: Basics
2. Day 2: Practice
3. Day 3: Intermediate
4. Day 4: Advanced
5. Day 5: Review"""