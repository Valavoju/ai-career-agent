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
                        📚 {item.skill || item.Skill}
                      </h4>

                      {(item.description ||
                        item.Description) && (
                        <p>
                          {item.description ||
                            item.Description}
                        </p>
                      )}

                      <p>
                        ⏳ {
                          item.estimated_time ||
                          item["Estimated Time"]
                        }
                      </p>

                      <div className="resource-grid">

                        {(item.resources ||
                          item.Resources ||
                          item["Learning Resources"] ||
                          []).map(
                            (
                              resource,
                              resourceIndex
                            ) => (

                              <div
                                key={resourceIndex}
                                className="resource-chip"
                              >
                                🔗 {resource}
                              </div>

                            )
                          )}

                      </div>

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