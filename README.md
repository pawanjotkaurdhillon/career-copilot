# AI Career Copilot

An AI-powered career assistant built using LangGraph, LangChain, and Groq.

The project helps users analyze resumes, search for relevant jobs, calculate resume-job fit scores, and identify skill gaps.

---

## Features

### Resume Retrieval
- Retrieve resume data using a resume ID.
- Store resume information in workflow state.

### Job Search
- Search jobs based on title, location, and experience.
- Store matching jobs in workflow state.

### Fit Score Analysis
- Compare resume skills with job requirements.
- Calculate a match percentage.
- Identify matched skills.

---

## Current Workflow

```text
User Query
    ↓
Planner
    ↓
Router
    ↓
Execution Node
    ↓
State Update
```

Example:

```text
User Request
    ↓
Search Jobs Node
    ↓
Jobs Stored in State
    ↓
Fit Score Node
    ↓
Fit Scores Stored in State
```

---

## Project Structure

```text
career-copilot/
│
├── app/
│   ├── graph.py
│   ├── nodes.py
│   ├── tools.py
│   ├── state.py
│   ├── schemas.py
│   ├── prompts.py
│   └── config.py
│
├── uploads/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Groq
- Pydantic

---

## Implemented Components

### Tools
- get_resume_text
- search_jobs
- calculate_fit_score

### Nodes
- Planner Node
- Search Jobs Node
- Resume Node
- Fit Score Node

---

## Upcoming Features

- Skill Gap Analysis
- LLM-based Planner
- FastAPI Backend
- REST API Endpoints
- Deployment

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/pawanjotkaurdhillon/career-copilot.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## Live Demo

https://career-copilot-82ro.onrender.com

API Docs:
https://career-copilot-82ro.onrender.com/docs

## Author

Pawanjot Kaur