from langchain.tools import tool
from pathlib import Path

UPLOAD_DIR = Path("uploads")


@tool
def get_resume_text(resume_id: str) -> str:
    """
    Return the extracted text for a resume.
    """

    text_file = UPLOAD_DIR / f"{resume_id}.txt"

    if not text_file.exists():
        return "Resume not found."

    return text_file.read_text(encoding="utf-8")


@tool
def search_jobs(
    job_title: str,
    location: str,
    experience: str
) -> list:
    """
    Search jobs matching title,
    location and experience.
    """

    try:
        experience = int(experience)
    except ValueError:
        experience = 0

    jobs = [
        {
            "title": "GenAI Engineer",
            "location": "Gurgaon",
            "experience": 0,
            "skills": [
                "Python",
                "LangChain",
                "LangGraph",
                "RAG"
            ]
        },
        {
            "title": "AI Engineer",
            "location": "Bangalore",
            "experience": 1,
            "skills": [
                "Python",
                "FastAPI",
                "Vector Databases"
            ]
        }
    ]

    matching_jobs = []

    for job in jobs:
        if (
            job_title.lower() in job["title"].lower()
            and job["location"] == location
            and job["experience"] <= experience
        ):
            matching_jobs.append(job)

    return matching_jobs

@tool
def calculate_fit_score(
    resume_text: str,
    job_skills: list
) -> dict:
    """
    Calculate fit score between resume and job.
    """

    resume_text = resume_text.lower()

    matched_skills = []

    for skill in job_skills:

        if skill.lower() in resume_text:
            matched_skills.append(skill)

    score = int(
        (len(matched_skills) / len(job_skills))
        * 100
    )

    return {
        "score": score,
        "matched_skills": matched_skills
    }

@tool
def analyze_skill_gap(
    resume_text: str,
    job_skills: list
) -> dict:
    """
    Identify missing skills between resume and job.
    """

    resume_text = resume_text.lower()

    missing_skills = []

    for skill in job_skills:

        if skill.lower() not in resume_text:
            missing_skills.append(skill)

    return {
        "missing_skills": missing_skills
    }       