from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from resume_parser import (
    extract_text,
    extract_email,
    extract_name
)

from resume_intelligence_agent import (
    generate_candidate_intelligence
)

from skill_extractor import extract_skills
from role_analyzer import get_role_requirements
from matcher import calculate_match
from roadmap import generate_roadmap
from advisor import get_hiring_recommendation

# NEW AGENTS
from communication_agent import generate_hr_email
from interview_scheduler import generate_interview_plan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():
    return {
        "status": "alive"
    }


@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    role: str = Form(...)
):

    # Save uploaded resume

    content = await file.read()

    with open(file.filename, "wb") as f:
        f.write(content)

    # Extract resume text

    resume_text = extract_text(file.filename)

    candidate_intelligence = (
        generate_candidate_intelligence(
            resume_text,
            role
        )
    )

    # Extract Candidate Information

    candidate_email = extract_email(resume_text)

    candidate_name = extract_name(resume_text)

    # Resume Analysis

    resume_analysis = extract_skills(resume_text)

    # Get role requirements

    role_analysis = get_role_requirements(role)

    # ATS Matching

    result = calculate_match(
        resume_analysis["skills"],
        role_analysis["required_skills"]
    )

    # Learning Roadmap

    roadmap = generate_roadmap(
        role,
        result["missing_skills"]
    )

    # Hiring Recommendation Agent

    recommendation = get_hiring_recommendation(
        result["match_score"],
        result["matching_skills"],
        result["missing_skills"],
        role,
        resume_text
)

    # Candidate Communication Agent

    communication_email = generate_hr_email(
        role,
        recommendation["recommendation"]
    )

    # Interview Scheduling Agent

    interview_plan = generate_interview_plan(
        role,
        recommendation["recommendation"],
        result["matching_skills"],
        result["missing_skills"]
)

    return {

        # Basic Information

        "role": role,

        "candidate_name": candidate_name,

        "candidate_email": candidate_email,

        # Resume Screening Agent

        

        "resume_skills":
            resume_analysis["skills"],

        "candidate_strengths":
            resume_analysis["strengths"],

        "recommended_role":
            resume_analysis["recommended_role"],

        "required_skills":
            role_analysis["required_skills"],

        "match_score":
            result["match_score"],

        # Skill Evaluation Agent

        "matching_skills":
            result["matching_skills"],

        "missing_skills":
            result["missing_skills"],

        # Hiring Recommendation Agent

        "recommendation":
            recommendation["recommendation"],

        "confidence":
            recommendation["confidence_percentage"],

        # Candidate Communication Agent

        "communication_email":
            communication_email,

        # Interview Scheduling Agent

        "interview_plan":
            interview_plan,

        "risk_level":
            recommendation["risk_level"],

        "assessment":
             recommendation["assessment"],

        "recommended_action":
            recommendation["action"],

        "candidate_intelligence":
            candidate_intelligence,

        # Career Roadmap

        "roadmap":
            roadmap
    }