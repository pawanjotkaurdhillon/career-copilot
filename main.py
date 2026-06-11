from langchain_core.messages import HumanMessage

from app.graph import graph


initial_state = {
    "messages": [
        HumanMessage(
            content="Calculate fit score"
        )
    ],

    "resume_id": "resume_123",

    "resume_text": """
Python
FastAPI
SQL
LangChain
""",

    "job_details": None,

    "jobs": [
        {
            "title": "GenAI Engineer",
            "skills": [
                "Python",
                "LangChain",
                "LangGraph",
                "RAG"
            ]
        }
    ],

    "fit_scores": [],

    "skill_gaps": [],

    "next_step": None
}

result = graph.invoke(initial_state)

print(result)