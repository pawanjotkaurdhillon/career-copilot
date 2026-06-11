from app.state import CareerCopilotState
from app.tools import search_jobs
from app.tools import get_resume_text
from app.tools import calculate_fit_score
from app.tools import  analyze_skill_gap



def planner_node(state):

    user_message = (
        state["messages"][-1]
        .content
        .lower()
    )

    if "analyze" in user_message:
        return {
            "workflow": "resume_analysis"
        }

    if "match" in user_message:
        return {
            "workflow": "career_copilot",

            "job_details": {
                "job_title": "GenAI",
                "location": "Gurgaon",
                "experience": "0"
            }
        }

    return {
        "workflow": "job_search",

        "job_details": {
            "job_title": "GenAI",
            "location": "Gurgaon",
            "experience": "0"
        }
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

def skill_gap_node(state: CareerCopilotState):

    print("Skill Gap Node Executed")

    resume_text = state["resume_text"]

    jobs = state["jobs"]

    skill_gaps = []

    for job in jobs:

        result = analyze_skill_gap.invoke(
            {
                "resume_text": resume_text,
                "job_skills": job["skills"]
            }
        )

        skill_gaps.append(
            {
                "job_title": job["title"],
                "missing_skills": result["missing_skills"]
            }
        )

    return {
        "skill_gaps": skill_gaps
    }

def response_node(state: CareerCopilotState):

    print("Response Node Executed")

    workflow = state["workflow"]

    # ------------------
    # Job Search
    # ------------------

    if workflow == "job_search":

        jobs = state["jobs"]

        if not jobs:
            return {
                "final_response": "No matching jobs found."
            }

        response = "Matching Jobs:\n\n"

        for job in jobs:

            response += (
                f"Title: {job['title']}\n"
                f"Location: {job['location']}\n"
                f"Experience: {job['experience']} years\n"
                f"Skills: {', '.join(job['skills'])}\n\n"
            )

        return {
            "final_response": response
        }

    # ------------------
    # Resume Analysis
    # ------------------

    if workflow == "resume_analysis":

        resume_text = state["resume_text"]

        return {
            "final_response":
            f"Resume Content:\n\n{resume_text}"
        }

    # ------------------
    # Career Copilot
    # ------------------

    fit_scores = state["fit_scores"]

    skill_gaps = state["skill_gaps"]

    if not fit_scores:
        return {
            "final_response": "No matching jobs found."
        }

    score_data = fit_scores[0]
    gap_data = skill_gaps[0]

    response = f"""
Job Title: {score_data["job_title"]}

Fit Score: {score_data["score"]}%

Matched Skills:
{", ".join(score_data["matched_skills"])}

Missing Skills:
{", ".join(gap_data["missing_skills"])}

Recommendation:
Focus on learning the missing skills to improve your job match.
"""

    return {
        "final_response": response
    }