from app.state import CareerCopilotState
from app.tools import search_jobs
from app.tools import get_resume_text
from app.tools import calculate_fit_score



def planner_node(state: CareerCopilotState):

    user_message = (
        state["messages"][-1]
        .content
        .lower()
    )

    if "job" in user_message:
        return {
            "next_step": "search_jobs",
            "job_details": {
                "job_title": "GenAI",
                "location": "Gurgaon",
                "experience": "0"
            }
        }

    return {
        "next_step": "fit_score"
    }


def search_jobs_node(state: CareerCopilotState):

    print("Search Jobs Node Executed")

    details = state["job_details"]

    jobs = search_jobs.invoke(
        {
            "job_title": details["job_title"],
            "location": details["location"],
            "experience": details["experience"]
        }
    )

    return {
        "jobs": jobs
    }

def resume_node(state: CareerCopilotState):

    print("Resume Node Executed")

    resume_text = get_resume_text.invoke(
        {
            "resume_id": state["resume_id"]
        }
    )

    return {
        "resume_text": resume_text
    }   

def fit_score_node(state: CareerCopilotState):

    print("Fit Score Node Executed")

    resume_text = state["resume_text"]

    jobs = state["jobs"]

    fit_scores = []

    for job in jobs:

        result = calculate_fit_score.invoke(
            {
                "resume_text": resume_text,
                "job_skills": job["skills"]
            }
        )

        fit_scores.append(
            {
                "job_title": job["title"],
                "score": result["score"],
                "matched_skills": result["matched_skills"]
            }
        )

    return {
        "fit_scores": fit_scores
    }     