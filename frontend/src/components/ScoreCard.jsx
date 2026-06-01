function ScoreCard({ score }) {

  const getStatus = () => {

    if(score >= 75)
      return "Strong Match";

    if(score >= 50)
      return "Good Match";

    return "Needs Improvement";
  };

  return (
    <div className="dashboard-card score-card">

      <h2>ATS Match Score</h2>

      <div
        className="score-circle"
        style={{ "--score": score }}
      >
        <div className="score-number">
          {score}%
        </div>
      </div>

      <p className="score-status">
        {getStatus()}
      </p>

    </div>
  );
}

export default ScoreCard;