import ReactMarkdown from "react-markdown";

function RoadmapCard({ roadmap }) {
  return (
    <div className="result-card">
      <h2>🧠 AI Roadmap</h2>

      <ReactMarkdown>
        {roadmap}
      </ReactMarkdown>
    </div>
  );
}

export default RoadmapCard;