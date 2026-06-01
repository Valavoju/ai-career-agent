function SkillsCard({ title, skills, color }) {
  return (
    <div className="dashboard-card skills-card">
      <h2>{title}</h2>

      {skills.length === 0 ? (
        <div className="empty-state">
          No skills found
        </div>
      ) : (
        <div className="skills-grid">
          {skills.map((skill, index) => (
            <span
              key={index}
              className={`skill-chip ${color}`}
            >
              {skill}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}

export default SkillsCard;