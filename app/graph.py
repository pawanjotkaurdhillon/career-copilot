from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.state import CareerCopilotState

from app.nodes import (
    planner_node,
    search_jobs_node,
    resume_node,
    fit_score_node,
    skill_gap_node,
    response_node
)


def workflow_router(state):

    return state["workflow"]


def after_search_jobs(state):

    if state["workflow"] == "job_search":
        return "response"

    return "resume"


def after_resume(state):

    if state["workflow"] == "resume_analysis":
        return "response"

    return "fit_score"


builder = StateGraph(
    CareerCopilotState
)

# ------------------
# Register Nodes
# ------------------

builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "search_jobs",
    search_jobs_node
)

builder.add_node(
    "resume",
    resume_node
)

builder.add_node(
    "fit_score",
    fit_score_node
)

builder.add_node(
    "skill_gap",
    skill_gap_node
)

builder.add_node(
    "response",
    response_node
)

# ------------------
# Start
# ------------------

builder.add_edge(
    START,
    "planner"
)

# ------------------
# Workflow Selection
# ------------------

builder.add_conditional_edges(
    "planner",
    workflow_router,
    {
        "career_copilot": "search_jobs",
        "resume_analysis": "resume",
        "job_search": "search_jobs"
    }
)

# ------------------
# Job Search Routing
# ------------------

builder.add_conditional_edges(
    "search_jobs",
    after_search_jobs,
    {
        "response": "response",
        "resume": "resume"
    }
)

# ------------------
# Resume Routing
# ------------------

builder.add_conditional_edges(
    "resume",
    after_resume,
    {
        "response": "response",
        "fit_score": "fit_score"
    }
)

# ------------------
# Career Copilot Flow
# ------------------

builder.add_edge(
    "fit_score",
    "skill_gap"
)

builder.add_edge(
    "skill_gap",
    "response"
)

# ------------------
# End
# ------------------

builder.add_edge(
    "response",
    END
)

graph = builder.compile()