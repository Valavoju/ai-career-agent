function VerdictCard({
  recommendation,
  confidence,
}) {

  let color = "#ef4444";

  if(recommendation === "Strong Hire"){
    color = "#22c55e";
  }

  else if(recommendation === "Hire"){
    color = "#3b82f6";
  }

  else if(recommendation === "Borderline"){
    color = "#f59e0b";
  }

  return (
    <div className="dashboard-card">

      <h2>
        🤖 Hiring Recommendation Agent
      </h2>

      <h1
        className="verdict-title"
        style={{ color }}
      >
        {recommendation}
      </h1>

      <p className="confidence">
        Confidence Score: {confidence}%
      </p>

    </div>
  );
}

export default VerdictCard;