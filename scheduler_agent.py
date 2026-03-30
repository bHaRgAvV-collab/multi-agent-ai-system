def scheduler_agent(tasks):
    schedule = []

    base_hour = 9

    for i, task in enumerate(tasks):
        start = base_hour + i * 2
        end = start + 2

        schedule.append({
            "day": task["day"],
            "task": task["task"],
            "time": f"{start}:00 - {end}:00"
        })

    return schedule