from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from resume_parser import extract_text
from skill_extractor import extract_skills
from role_analyzer import get_role_requirements
from matcher import calculate_match
from roadmap import generate_roadmap

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    role: str = Form(...)
):

    content = await file.read()

    with open(file.filename, "wb") as f:
        f.write(content)

    resume_text = extract_text(file.filename)

    resume_analysis = extract_skills(resume_text)

    role_analysis = get_role_requirements(role)

    result = calculate_match(
        resume_analysis["skills"],
        role_analysis["required_skills"]
    )

    roadmap = generate_roadmap(
        role,
        result["missing_skills"]
    )

    return {
        "role": role,

        "resume_skills":
            resume_analysis["skills"],

        "required_skills":
            role_analysis["required_skills"],

        "match_score":
            result["match_score"],

        "matching_skills":
            result["matching_skills"],

        "missing_skills":
            result["missing_skills"],

        "roadmap":
            roadmap
    }