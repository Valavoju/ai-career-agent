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

              {plan.rounds.map(
                (round, index) => (

                  <div
                    key={index}
                    className="round-card"
                  >

                    <h4>
                      🎯 {round.round}
                    </h4>

                    <p>
                      <strong>
                        ⏳ Duration:
                      </strong>{" "}
                      {round.duration}
                    </p>

                    <p>
                      {round.description}
                    </p>

                  </div>
                )
              )}

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

              {plan.slots.map(
                (slot, index) => (

                  <div
                    key={index}
                    className="slot-card"
                  >
                    {typeof slot === "object"
                      ? JSON.stringify(slot)
                      : slot}
                  </div>

                )
              )}

            </div>
          </>
        )}

      {plan.message && (
        <div className="interview-message">
          <p>{plan.message}</p>
        </div>
      )}

    </div>
  );
}

export default InterviewCard;