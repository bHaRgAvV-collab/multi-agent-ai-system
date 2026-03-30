# 🚀 Multi-Agent AI Task Management System

## 📌 Overview

This project is a **Multi-Agent AI System** that helps users manage tasks, schedules, and information by coordinating multiple intelligent agents.

The system takes a user goal (e.g., *"Prepare for coding interview in 5 days"*) and processes it through a pipeline of specialized agents to generate a structured, actionable plan.

---

## 🧠 System Architecture

The system is built using a **Primary Orchestrator Agent** that coordinates the following sub-agents:

### 🔹 Planner Agent

* Converts user goals into structured step-by-step plans

### 🔹 Task Agent

* Breaks plans into structured tasks
* Stores tasks in a JSON-based database

### 🔹 Scheduler Agent

* Assigns time slots to tasks
* Converts tasks into a daily schedule

### 🔹 Memory Agent

* Stores past workflows (goal + schedule)
* Enables retrieval of previous data

---

## ⚙️ Workflow

```text
User Input → Orchestrator → Planner → Task → Scheduler → Memory → Output
```

Example:

> "Prepare for coding interview in 5 days"

Output:

* Day-wise plan
* Structured tasks
* Scheduled time slots
* Stored history

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Language:** Python
* **Data Storage:** JSON (simulating database)
* **AI Integration:** Gemini API (with fallback logic)

---

## 📂 Project Structure

```
├── main.py
├── orchestrator.py
├── planner_agent.py
├── task_agent.py
├── scheduler_agent.py
├── memory_agent.py
├── task_db.json
├── memory.json
```

---

## 🚀 API Endpoints

### ▶️ Run Workflow

```
POST /run
```

**Request:**

```json
{
  "query": "Prepare for coding interview in 5 days"
}
```

**Response:**

* Goal
* Planner output
* Task list
* Scheduled tasks
* Final response

---

### 🧠 Retrieve Memory

```
GET /memory
```

Returns previously stored workflows.

---

## ✨ Key Features

* Multi-agent coordination system
* Modular and extensible architecture
* Structured workflow execution
* Persistent memory storage
* Real-time API interaction

---

## 🔥 Highlights

* Designed a **multi-agent orchestration system**
* Implemented **end-to-end workflow automation**
* Built with **scalable and modular architecture**
* Handles **multi-step reasoning and task execution**

---

## 📌 Future Improvements

* Integration with real calendar APIs
* Database (MongoDB / PostgreSQL)
* Frontend dashboard (React / Streamlit)
* Authentication and user-specific memory

---

## 🧑‍💻 Author

Built as part of the **Gen AI APAC Edition Project**

---

## ⭐ Final Note

This project demonstrates how multiple AI agents can collaborate to solve real-world problems by breaking down complex goals into structured, actionable workflows.
