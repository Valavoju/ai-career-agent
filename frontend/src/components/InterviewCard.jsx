function InterviewCard({ slots }) {
  return (
    <div className="dashboard-card interview-card">

      <h2>📅 Interview Scheduling Agent</h2>

      <div className="slots-container">

        {slots?.map((slot, index) => (
          <div
            key={index}
            className="slot-item"
          >
            {slot}
          </div>
        ))}

      </div>

    </div>
  );
}

export default InterviewCard;