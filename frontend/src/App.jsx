import { useState, useEffect } from "react";
import axios from "axios";

import Hero from "./components/Hero";
import UploadSection from "./components/UploadSection";
import ScoreCard from "./components/ScoreCard";
import SkillsCard from "./components/SkillsCard";
import VerdictCard from "./components/VerdictCard";
import RoadmapCard from "./components/RoadmapCard";
import ResumeSummaryCard from "./components/ResumeSummaryCard";

import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("AI Engineer");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  // Wake up Render backend when app loads
  useEffect(() => {
    axios
      .get("https://ai-career-agent-yord.onrender.com/")
      .catch(() => {});
  }, []);

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

      console.log("Backend Response:", response.data);

    } catch (error) {
      console.error(error);

      if (error.response) {
        console.log(
          `Backend Error: ${error.response.status}`
        );
      } else {
        console.log(
          "Backend waking up..."
        );
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

      {loading && (
        <div className="loading-card">
          <h3>🤖 Connecting to Recruitment AI...</h3>

          <p>
            First request may take 20–30 seconds while
            the backend wakes up.
          </p>
        </div>
      )}

      {result && (
        <div className="results-container">

          <ScoreCard
            score={result.match_score}
          />

          <ResumeSummaryCard
            summary={`Your resume matches ${result.match_score}% of the selected role requirements. You currently possess ${
              result.matching_skills?.length || 0
            } matching skills and need to improve ${
              result.missing_skills?.length || 0
            } important skills to become more competitive for the ${role} role.`}
          />

          <VerdictCard
            score={result.match_score}
          />

          <SkillsCard
            title="✅ Matching Skills"
            skills={result.matching_skills || []}
            color="green"
          />

          <SkillsCard
            title="❌ Missing Skills"
            skills={result.missing_skills || []}
            color="red"
          />

          <RoadmapCard
            roadmap={result.roadmap}
          />

        </div>
      )}

      <footer className="footer">
        © 2026 CareerPilot AI • Built by Avinash
      </footer>
    </div>
  );
}

export default App;