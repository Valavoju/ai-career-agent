function VerdictCard({ score }) {

  let verdict = "";
  let confidence = "";

  if(score >= 75){
    verdict = "Strong Hire";
    confidence = "95%";
  }

  else if(score >= 55){
    verdict = "Hire";
    confidence = "85%";
  }

  else if(score >= 30){
    verdict = "Borderline";
    confidence = "75%";
  }

  else{
    verdict = "Needs Upskilling";
    confidence = "70%";
  }

  return (
    <div className="dashboard-card">

      <h2>🤖 Hiring Recommendation</h2>

      <h1 className="verdict-title">
        {verdict}
      </h1>

      <p className="confidence">
        Confidence: {confidence}
      </p>

    </div>
  );
}

export default VerdictCard;