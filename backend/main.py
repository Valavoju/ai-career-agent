from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from resume_parser import extract_text
from skill_extractor import extract_skills
from role_analyzer import get_role_requirements
from matcher import calculate_match
from roadmap import generate_roadmap
from advisor import get_hiring_recommendation

# NEW AGENTS
from communication_agent import generate_hr_email
from interview_scheduler import generate_interview_slots

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

    # Extract candidate skills

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
        result["match_score"]
    )

    # Candidate Communication Agent

    communication_email = generate_hr_email(
        role,
        recommendation["recommendation"]
    )

    # Interview Scheduling Agent

    interview_slots = generate_interview_slots()

    return {

        # Basic Information

        "role": role,

        # Resume Screening Agent

        "resume_skills":
            resume_analysis["skills"],

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
            recommendation["confidence"],

        # Candidate Communication Agent

        "communication_email":
            communication_email,

        # Interview Scheduling Agent

        "interview_slots":
            interview_slots,

        # Career Roadmap

        "roadmap":
            roadmap
    }