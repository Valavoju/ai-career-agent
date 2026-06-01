function ScoreCard({ score }) {

  let label = "Needs Improvement";
  let color = "#ef4444";

  if (score >= 75) {
    label = "Excellent Match";
    color = "#22c55e";
  }

  else if (score >= 55) {
    label = "Good Match";
    color = "#3b82f6";
  }

  else if (score >= 30) {
    label = "Average Match";
    color = "#f59e0b";
  }

  return (
    <div className="dashboard-card score-card">

      <h2>🎯 ATS Match Score</h2>

      <div
        className="score-number"
        style={{ color }}
      >
        {score}%
      </div>

      <div className="score-bar">
        <div
          className="score-fill"
          style={{
            width: `${score}%`,
            background: color,
          }}
        />
      </div>

      <div
        className="score-label"
        style={{ color }}
      >
        {label}
      </div>

    </div>
  );
}

export default ScoreCard;