function InterviewCard({ plan }) {

  console.log("INTERVIEW PLAN =", plan);

  if (!plan) {
    return (
      <div className="dashboard-card">
        <h2>📅 Interview Scheduling Agent</h2>
        <p>No interview data available.</p>
      </div>
    );
  }

  return (
    <div className="dashboard-card">

      <h2>
        📅 Interview Scheduling Agent
      </h2>

      <div className="interview-summary">

        <p>
          <strong>🎯 Difficulty:</strong>{" "}
          {plan.difficulty}
        </p>

        <p>
          <strong>⏳ Duration:</strong>{" "}
          {plan.duration}
        </p>

      </div>

      {Array.isArray(plan.rounds) &&
        plan.rounds.length > 0 && (
          <>
            <h3>
              🚀 Interview Rounds
            </h3>

            <div className="rounds-grid">

              {plan.rounds.map((round, index) => (

                <div
                  key={index}
                  className="round-card"
                >

                 <h4 className="round-title">
  🎯 {round.round_name || round.round_type || "Interview Round"}
</h4>

<p className="round-duration">
  ⏳ {round.duration || "N/A"}
</p>

<p className="round-description">
  {round.round_type}
</p>

                </div>

              ))}

            </div>
          </>
        )}

      {Array.isArray(plan.focus_areas) &&
        plan.focus_areas.length > 0 && (
          <>
            <h3>
              🎯 Focus Areas
            </h3>

            <div className="focus-grid">

              {plan.focus_areas.map((area, index) => (

                <div
                  key={index}
                  className="focus-card"
                >

                  <h4>
                    📚 {area.area}
                  </h4>

                  <p>
                    {area.description}
                  </p>

                </div>

              ))}

            </div>
          </>
        )}

      {Array.isArray(plan.slots) &&
        plan.slots.length > 0 && (
          <>
            <h3>
              📆 Available Slots
            </h3>

            <div className="slots-grid">

              {plan.slots.map((slot, index) => (

                <div
                  key={index}
                  className="slot-card"
                >
                  {typeof slot === "object"
                    ? JSON.stringify(slot)
                    : slot}
                </div>

              ))}

            </div>
          </>
        )}

      {plan.strategy && (

        <div className="career-outcome">

          <h3>
            🎯 Interview Strategy
          </h3>

          <p>
            {plan.strategy}
          </p>

        </div>

      )}

    </div>
  );
}

export default InterviewCard;