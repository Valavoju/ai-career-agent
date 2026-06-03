import { useState, useEffect } from "react";
import axios from "axios";

import Sidebar from "./components/Sidebar";
import Navbar from "./components/Navbar";
import emailjs from "@emailjs/browser";
import UploadSection from "./components/UploadSection";
import ScoreCard from "./components/ScoreCard";
import SkillsCard from "./components/SkillsCard";
import VerdictCard from "./components/VerdictCard";
import RoadmapCard from "./components/RoadmapCard";
import ResumeSummaryCard from "./components/ResumeSummaryCard";
import InterviewCard from "./components/InterviewCard";
import CandidateIntelligenceCard
from "./components/CandidateIntelligenceCard";

import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("AI Engineer");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const [activeTab, setActiveTab] = useState("dashboard");

  useEffect(() => {
    axios.get("https://ai-career-agent-yord.onrender.com/").catch(() => {});
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

  const sendEmail = (data) => {
    if (!data.candidate_email) {
      console.log("No email address found in resume");
      return;
    }

    console.log("Candidate Name:", data.candidate_name);
    console.log("Candidate Email:", data.candidate_email);

    emailjs
      .send(
        "service_y2xmyd4",
        "template_fecm0dj",
        {
          candidate_name: data.candidate_name,

          to_email: data.candidate_email,

          role: data.role,

          score: data.match_score,

          recommendation: data.recommendation,

          confidence: data.confidence,

          matching_skills: data.matching_skills.join(", "),

          missing_skills: data.missing_skills.join(", "),

          roadmap: data.roadmap,
        },

        "kYNRgwz1CN6SWMunc",
      )
      .then(() => {

  alert(
    `Report successfully sent to ${data.candidate_email}`
  );

  console.log(
    `Report sent to ${data.candidate_email}`
  );

})
      .catch((error) => {
        console.error("EmailJS Error:", error);
      });
  };

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
        },
      );
      setResult(response.data);

      console.log(response.data);
      console.log("ROADMAP =", response.data.roadmap);
      console.log(response.data.interview_plan);

      if (response.data.candidate_email) {
        sendEmail(response.data);
      }

      console.log("Backend Response:", response.data);
    } catch (error) {
      console.error(error);

      if (error.response) {
        alert(`Backend Error: ${error.response.status}`);
      } else {
        alert("Backend is waking up. Please wait 20-30 seconds and try again.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard-layout">
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />

      <div className="main-content">
        <Navbar />

        {activeTab === "dashboard" && (
  <UploadSection
    file={file}
    setFile={setFile}
    role={role}
    setRole={setRole}
    roles={roles}
    analyzeResume={analyzeResume}
    loading={loading}
  />
)}

        {loading && (
          <div className="loading-card">
            <h3>🤖 Recruitment AI Processing...</h3>

            <p>
              Resume screening, skill evaluation, hiring recommendation and
              interview scheduling are running...
            </p>
          </div>
        )}

        {result && (
          <div className="results-container">
            {/* DASHBOARD */}

            {activeTab === "dashboard" && (
              <>
                <div className="top-grid">
                  <ScoreCard score={result.match_score} />

                  <VerdictCard
                    recommendation={result.recommendation}
                    confidence={result.confidence}
                  />
                </div>

                <ResumeSummaryCard
                  summary={`Your resume matches ${result.match_score}% of the selected role requirements. You currently possess ${
                    result.matching_skills?.length || 0
                  } matching skills and need to improve ${
                    result.missing_skills?.length || 0
                  } important skills to become more competitive for the ${role} role.`}
                />

                <CandidateIntelligenceCard
  intelligence={result.candidate_intelligence}
/>
              </>
            )}

            {/* SCREENING */}

            {activeTab === "screening" && (
              <>
                <ResumeSummaryCard
                  summary={`Your resume matches ${result.match_score}% of the selected role requirements. You currently possess ${
                    result.matching_skills?.length || 0
                  } matching skills and need to improve ${
                    result.missing_skills?.length || 0
                  } important skills.`}
                />

                <ScoreCard score={result.match_score} />
              </>
            )}

            {/* SKILLS */}

            {activeTab === "skills" && (
              <>
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

                <RoadmapCard roadmap={result.roadmap} />
              </>
            )}

            {/* INTERVIEW */}

            {activeTab === "interview" && (
  <InterviewCard
    plan={result.interview_plan}
  />
)}

            {/* HIRING */}

            {activeTab === "hiring" && (
              <VerdictCard
                recommendation={result.recommendation}
                confidence={result.confidence}
              />
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
