function CandidateIntelligenceCard({ intelligence }) {

  if (!intelligence) return null;

  return (
    <div className="dashboard-card">

      <h2>🧠 Candidate Intelligence Agent</h2>

      <div className="intelligence-section">

        <h3>📄 Executive Summary</h3>

        <p>
          {intelligence.profile_summary}
        </p>

      </div>

      <div className="intelligence-section">

        <h3>💪 Strengths</h3>

        <ul>
          {intelligence.strengths?.map((item, index) => (
            <li key={index}>
              {item}
            </li>
          ))}
        </ul>

      </div>

      <div className="intelligence-section">

        <h3>⚠ Improvement Areas</h3>

        <ul>
          {intelligence.weaknesses?.map((item, index) => (
            <li key={index}>
              {item}
            </li>
          ))}
        </ul>

      </div>

      <div className="intelligence-section">

        <h3>🚀 Recommended Career Path</h3>

        <p>
          {intelligence.career_path}
        </p>

      </div>

    </div>
  );
}

export default CandidateIntelligenceCard;