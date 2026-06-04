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

      {Object.entries(roadmap.roadmap).map(
        ([phaseName, topics], phaseIndex) => (

          <div
            className="phase-card"
            key={phaseIndex}
          >

            <h3>
              🚀 {phaseName}
            </h3>

            {Object.entries(topics).map(
  ([skillName, skillData], topicIndex) => (

              <div
                key={topicIndex}
                className="roadmap-topic"
              >

                <h4>
  {skillName}
</h4>

<pre>
  {JSON.stringify(skillData, null, 2)}
</pre>

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