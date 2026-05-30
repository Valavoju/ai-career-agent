function ScoreCard({ score }) {
  return (
    <div className="result-card">

      <h2>🎯 ATS Match Score</h2>

      <div
        className="score-circle"
        style={{ "--score": score }}
      >
        <div className="score-number">
          {score}%
        </div>
      </div>

    </div>
  );
}

export default ScoreCard;