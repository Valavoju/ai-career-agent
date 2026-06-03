function RoadmapCard({ roadmap }) {

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

      <div className="phase-card">

        <h3>
          🚀 Phase 1
        </h3>

        <p>
          Duration: {roadmap.roadmap.phase1.duration}
        </p>

        <ul>
          {roadmap.roadmap.phase1.tasks.map(
            (task, index) => (
              <li key={index}>
                {task.title}
              </li>
            )
          )}
        </ul>

      </div>

      <div className="phase-card">

        <h3>
          🚀 Phase 2
        </h3>

        <p>
          Duration: {roadmap.roadmap.phase2.duration}
        </p>

        <ul>
          {roadmap.roadmap.phase2.tasks.map(
            (task, index) => (
              <li key={index}>
                {task.title}
              </li>
            )
          )}
        </ul>

      </div>

      <div className="phase-card">

        <h3>
          🚀 Phase 3
        </h3>

        <p>
          Duration: {roadmap.roadmap.phase3.duration}
        </p>

        <ul>
          {roadmap.roadmap.phase3.tasks.map(
            (task, index) => (
              <li key={index}>
                {task.title}
              </li>
            )
          )}
        </ul>

      </div>

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