from langgraph.graph import MessagesState


class CareerCopilotState(MessagesState):
    resume_id: str | None
    resume_text: str | None

    job_details: dict | None

    jobs: list

    fit_scores: list

    skill_gaps: list

    next_step: str | None