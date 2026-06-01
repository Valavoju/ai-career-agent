function ResumeSummaryCard({ summary }) {
  return (
    <div className="dashboard-card">

      <h2>📄 Candidate Summary</h2>

      <p className="summary-text">
        {summary}
      </p>

    </div>
  );
}

export default ResumeSummaryCard;