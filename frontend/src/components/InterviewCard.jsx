function InterviewCard({ plan }) {
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
      <h2>📅 Interview Scheduling Agent</h2>

      <p>
        <strong>Difficulty:</strong> {plan.difficulty}
      </p>

      <p>
        <strong>Duration:</strong> {plan.duration}
      </p>

      {plan.rounds?.length > 0 && (
        <>
          <h3>Interview Rounds</h3>

          <div className="rounds-grid">
            {plan.rounds.map((round, index) => (
              <div key={index} className="round-card">
                {round}
              </div>
            ))}
          </div>
        </>
      )}

      {plan.slots?.length > 0 && (
        <>
          <h3>Available Slots</h3>

          <div className="slots-grid">
            {plan.slots.map((slot, index) => (
              <div key={index} className="slot-card">
                {slot}
              </div>
            ))}
          </div>
        </>
      )}

      {plan.message && <p>{plan.message}</p>}
    </div>
  );
}

export default InterviewCard;
