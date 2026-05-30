function VerdictCard({ score }) {

  let verdict = "";

  if(score >= 80){
    verdict = "🚀 Job Ready";
  }

  else if(score >= 60){
    verdict = "⚡ Almost Ready";
  }

  else{
    verdict = "📚 Need Upskilling";
  }

  return (
    <div className="result-card">

      <h2>🤖 AI Verdict</h2>

      <p>{verdict}</p>

    </div>
  );
}

export default VerdictCard;