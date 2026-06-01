function ResumeSummaryCard({ summary }) {
  return (
    <div className="dashboard-card summary-card">
      <h2>📄 Candidate Summary</h2>

      <div className="summary-content">
        <p>{summary}</p>
      </div>
    </div>
  );
}

export default ResumeSummaryCard;