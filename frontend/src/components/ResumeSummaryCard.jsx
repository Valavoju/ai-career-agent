function ResumeSummaryCard({ summary }) {
  return (
    <div className="result-card">
      <h2>📄 Resume Summary</h2>

      <div className="roadmap">
        {summary}
      </div>
    </div>
  );
}

export default ResumeSummaryCard;