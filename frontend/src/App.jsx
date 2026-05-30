import { useState } from "react";
import axios from "axios";

import Hero from "./components/Hero";
import UploadSection from "./components/UploadSection";
import ScoreCard from "./components/ScoreCard";
import SkillsCard from "./components/SkillsCard";
import VerdictCard from "./components/VerdictCard";
import RoadmapCard from "./components/RoadmapCard";

import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("AI Engineer");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const roles = [
    "AI Engineer",
    "Machine Learning Engineer",
    "Data Scientist",
    "Software Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "Cloud Engineer",
    "DevOps Engineer",
    "Cyber Security Analyst",
    "Java Developer",
    "Python Developer",
    "React Developer",
  ];

  const analyzeResume = async () => {
    if (!file) {
      alert("Please upload your resume");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);
      formData.append("role", role);

      const response = await axios.post(
        "https://ai-career-agent-yord.onrender.com/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);

      console.log(response.data);
    } catch (error) {
      console.error(error);

      if (error.response) {
        alert(`Backend Error: ${error.response.status}`);
      } else {
        alert("Network Error");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <Hero />

      <UploadSection
        file={file}
        setFile={setFile}
        role={role}
        setRole={setRole}
        roles={roles}
        analyzeResume={analyzeResume}
        loading={loading}
      />

      {result && (
        <div className="results-container">
          <div className="result-card">
            <h2>🎯 Match Score</h2>
            <h1>{result.match_score}%</h1>
          </div>

          <div className="result-card">
            <h2>✅ Matching Skills</h2>

            <div className="skills">
              {result.matching_skills?.map((skill, index) => (
                <span key={index} className="skill-chip success">
                  {skill}
                </span>
              ))}
            </div>
          </div>

          <div className="result-card">
            <h2>❌ Missing Skills</h2>

            <div className="skills">
              {result.missing_skills?.map((skill, index) => (
                <span key={index} className="skill-chip danger">
                  {skill}
                </span>
              ))}
            </div>
          </div>

          <div className="result-card">
            <h2>🧠 AI Roadmap</h2>

            <div className="roadmap">
              {result.roadmap}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;