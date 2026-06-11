from langgraph.graph import MessagesState


class CareerCopilotState(MessagesState):

    workflow: str | None


    resume_id: str | None
    resume_text: str | None

    job_details: dict | None

    jobs: list

    fit_scores: list

    skill_gaps: list

    final_response: str | None

    next_step: str | None