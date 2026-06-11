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
    fit_score_node
)


def router(state):
    return state["next_step"]


builder = StateGraph(
    CareerCopilotState
)

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

builder.add_edge(
    START,
    "planner"
)

builder.add_conditional_edges(
    "planner",
    router
)

builder.add_edge(
    "fit_score",
    END
)

graph = builder.compile()