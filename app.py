import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.sidebar.title("⚙️ Controls")
st.sidebar.markdown("Manage your AI workflow")

if st.sidebar.button("🔄 Reset"):
    st.rerun()

st.set_page_config(page_title="AI Task Manager", layout="wide")

st.markdown("""
# 🧠 Multi-Agent AI Task Manager
### Plan smarter. Execute faster.
""")

goal = st.text_input("Enter your goal:")
st.info("🧠 Planner → 📝 Task → ⏱ Scheduler → 💾 Memory")

if st.button("Generate Plan 🚀"):
    if goal:
        with st.spinner("🤖 Multi-agent system processing your request..."):
            try:
                response = requests.post(
                    f"{API_URL}/run",
                    json={"goal": goal},
                    timeout=10
                )
                data = response.json()

                st.success("Plan generated!")

                # ---- GOAL ----
                st.subheader("🎯 Goal")
                st.write(data.get("goal", ""))
                
                # ---- PLAN ----
                st.subheader("📅 Plan")

                steps = data.get("steps", [])

                # 🔥 Extract Scheduler output
                schedule = []
                for step in steps:
                    if step.get("agent") == "Scheduler":
                        schedule = step.get("output", [])

                # ---- DISPLAY SCHEDULE ----
                if schedule:
                    for item in schedule:
                         with st.container():
                          st.markdown(f"""
                         ### 📌 {item['day']}  
                         **📝 Task:** {item['task']}  
                        **⏰ Time:** {item['time']}
                        """)
                    st.divider()
                else:
                    st.warning("No schedule found")

                # ---- SUMMARY ----
                st.subheader("🧾 Summary")
                st.write(data.get("final_response", ""))

            except Exception as e:
                st.error(f"Error: {e}")