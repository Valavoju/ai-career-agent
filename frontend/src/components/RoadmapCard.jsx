import ReactMarkdown from "react-markdown";

function RoadmapCard({ roadmap }) {
  return (
    <div className="dashboard-card roadmap-card">
      <h2>🧠 Learning Roadmap Agent</h2>

      <div className="roadmap-content">
        <ReactMarkdown>{roadmap}</ReactMarkdown>
      </div>
    </div>
  );
}

export default RoadmapCard;