function RoadmapCard({ roadmap }) {

  if (!roadmap) {
    return null;
  }

  return (
    <div className="dashboard-card">

      <h2>🧠 AI Learning Roadmap</h2>

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
          ([phaseName, phaseData], phaseIndex) => (

            <div
              className="phase-card"
              key={phaseIndex}
            >

              <h3>
                🚀 {phaseName}
              </h3>

              <div className="skills-grid">

                {Array.isArray(phaseData) &&
                  phaseData.map((item, index) => (

                    <div
                      key={index}
                      className="roadmap-skill-card"
                    >

                      <h4>
                        📚 {item.topic}
                      </h4>

                      <p>
                        ⏳ {item["estimated time"]}
                      </p>

                      {item.subtopics && (

                        <>
                          <h5>Topics Covered</h5>

                          <div className="subtopic-grid">

                            {item.subtopics.map(
                              (subtopic, i) => (

                                <span
                                  key={i}
                                  className="skill-chip"
                                >
                                  ✅ {subtopic}
                                </span>

                              )
                            )}

                          </div>
                        </>

                      )}

                      {item["learning resources"] && (

                        <>
                          <h5>Learning Resources</h5>

                          <div className="resource-grid">

                            {item["learning resources"].map(
                              (resource, i) => (

                                <div
                                  key={i}
                                  className="resource-chip"
                                >
                                  🔗 {resource}
                                </div>

                              )
                            )}

                          </div>
                        </>

                      )}

                    </div>

                  ))}

              </div>

            </div>

          )
        )}

      <div className="career-outcome">

        <h3>
          🎯 Career Outcome
        </h3>

        <p>
          {roadmap.expected_outcome}
        </p>

      </div>

    </div>
  );
}

export default RoadmapCard;