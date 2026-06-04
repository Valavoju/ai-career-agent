function RoadmapCard({ roadmap }) {

  console.log("ROADMAP DATA =", roadmap);

  if (!roadmap) return null;

  return (
    <div className="dashboard-card">

      <h2>
        🧠 AI Learning Roadmap
      </h2>

      <div className="roadmap-header">

        <div className="roadmap-stat">
          <h3>📊 Readiness</h3>
          <p>{roadmap.readiness}</p>
        </div>

        <div className="roadmap-stat">
          <h3>⏳ Estimated Time</h3>
          <p>{roadmap.estimated_time}</p>
        </div>

      </div>

      {roadmap.roadmap &&
        Object.entries(roadmap.roadmap).map(
          ([phaseName, topics], phaseIndex) => (

            <div
              className="phase-card"
              key={phaseIndex}
            >

              <h3>
                🚀 {phaseName}
              </h3>

              {Array.isArray(topics) &&
                topics.map((topic, topicIndex) => (

                  <div
                    key={topicIndex}
                    className="roadmap-topic"
                  >

                    <h4>
                      📚 {topic.skill}
                    </h4>

                    <p>
                      {topic.description}
                    </p>

                    <p>
                      <strong>
                        ⏳ Estimated Time:
                      </strong>{" "}
                      {topic.estimated_time}
                    </p>

                    {topic.resources &&
                      topic.resources.length > 0 && (

                       <div className="resource-section">

  <strong>
    🔗 Learning Resources:
  </strong>

  {topic.resources.map((resource, index) => (

    <p
      key={index}
      className="resource-item"
    >
      • {resource}
    </p>

  ))}

</div>

                      )}

                  </div>

                ))}

            </div>

          )
        )}

      <div className="career-outcome">

        <h3>
          🎯 Expected Outcome
        </h3>

        <p>
          {roadmap.expected_outcome}
        </p>

      </div>

    </div>
  );
}

export default RoadmapCard;