function VerdictCard({
  recommendation,
  confidence,
}) {

  let color = "#ef4444";
  let insight = "";
  let action = "";

  if (recommendation === "Strong Hire") {

    color = "#22c55e";

    insight =
      "The candidate demonstrates strong alignment with the selected role and possesses most of the required technical competencies.";

    action =
      "Proceed directly to advanced technical and managerial interview rounds.";
  }

  else if (recommendation === "Hire") {

    color = "#3b82f6";

    insight =
      "The candidate satisfies the majority of role requirements and shows good potential for successful onboarding.";

    action =
      "Schedule technical and HR interviews for further evaluation.";
  }

  else if (recommendation === "Borderline") {

    color = "#f59e0b";

    insight =
      "The candidate has foundational skills but lacks several important competencies required for the target role.";

    action =
      "Conduct a skill assessment before proceeding with recruitment.";
  }

  else {

    insight =
      "The candidate currently does not meet the minimum skill requirements for the selected role.";

    action =
      "Recommend completion of the learning roadmap before reapplying.";
  }

  return (
    <div className="dashboard-card">

      <h2>
        🤖 Recruitment Decision Agent
      </h2>

      <h1
        className="verdict-title"
        style={{ color }}
      >
        {recommendation}
      </h1>

      <p className="confidence">
  Recruiter Confidence: {Math.round(confidence * 100)}%
</p>

      <div className="ai-insight">

        <h3>
          🧠 AI Assessment
        </h3>

        <p>
          {insight}
        </p>

      </div>

      <div className="ai-action">

        <h3>
          🎯 Recommended Action
        </h3>

        <p>
          {action}
        </p>

      </div>

    </div>
  );
}

export default VerdictCard;