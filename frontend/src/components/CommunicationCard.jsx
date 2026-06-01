function CommunicationCard({ email }) {
  return (
    <div className="dashboard-card communication-card">

      <h2>📧 Candidate Communication Agent</h2>

      <div className="email-content">
        {email}
      </div>

    </div>
  );
}

export default CommunicationCard;