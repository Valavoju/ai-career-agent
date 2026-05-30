import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("AI Engineer");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

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
    "React Developer"
  ];

  const analyzeResume = async () => {
    if (!file) {
      alert("Please upload a resume");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);
    formData.append("role", role);

    try {
      const response = await axios.post(
        "https://ai-career-agent-yord.onrender.com/analyze",
        formData
      );

      setResult(response.data);
    } catch (error) {
  console.log("FULL ERROR:", error);
  console.log("RESPONSE:", error.response);
  console.log("DATA:", error.response?.data);

  alert(
    JSON.stringify(
      error.response?.data || error.message,
      null,
      2
    )
  );
}

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AI Career Research Agent</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <select
        value={role}
        onChange={(e) => setRole(e.target.value)}
      >
        {roles.map((r) => (
          <option key={r}>{r}</option>
        ))}
      </select>

      <button onClick={analyzeResume}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {result && (
        <div className="result">
          <h2>Match Score: {result.match_score}%</h2>

          <h3>Matching Skills</h3>
          <ul>
            {result.matching_skills?.map((skill) => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>

          <h3>Missing Skills</h3>
          <ul>
            {result.missing_skills?.map((skill) => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>

          <h3>Roadmap</h3>
          <p>{result.roadmap}</p>
        </div>
      )}
    </div>
  );
}

export default App;