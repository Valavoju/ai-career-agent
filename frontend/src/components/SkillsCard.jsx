function SkillsCard({ title, skills, color }) {

  return (
    <div className="dashboard-card">

      <h2>{title}</h2>

      <div className="skills-grid">

        {skills.length === 0 ? (
          <p>No skills found</p>
        ) : (
          skills.map((skill) => (
            <span
              key={skill}
              className={`skill-chip ${color}`}
            >
              {skill}
            </span>
          ))
        )}

      </div>

    </div>
  );
}

export default SkillsCard;