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

          <ul>
            {plan.rounds.map((round, index) => (
              <li key={index}>
                {round}
              </li>
            ))}
          </ul>
        </>
      )}

      {plan.slots?.length > 0 && (
        <>
          <h3>Available Slots</h3>

          <ul>
            {plan.slots.map((slot, index) => (
              <li key={index}>
                {slot}
              </li>
            ))}
          </ul>
        </>
      )}

      {plan.message && (
        <p>
          {plan.message}
        </p>
      )}

    </div>
  );
}

export default InterviewCard;