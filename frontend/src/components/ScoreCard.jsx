import "./ScoreCard.css";

function ScoreCard({ score }) {
  return (
    <div className="score-card">
      <div className="circle">
        <h1>{score}%</h1>
      </div>

      <h2>ATS Match Score</h2>
    </div>
  );
}

export default ScoreCard;