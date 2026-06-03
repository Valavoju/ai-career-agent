function CandidateIntelligenceCard({ data }) {

  if (!data) return null;

  return (
    <div className="dashboard-card">

      <h2>🧠 Candidate Intelligence Agent</h2>

      <h3>Executive Summary</h3>

      <p>{data.profile_summary}</p>

      <h3>💪 Strength Areas</h3>

      <ul>
        {data.strengths?.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

      <h3>⚠ Improvement Areas</h3>

      <ul>
        {data.weaknesses?.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>

      <h3>🚀 Recommended Career Path</h3>

      <p>{data.career_path}</p>

    </div>
  );
}

export default CandidateIntelligenceCard;