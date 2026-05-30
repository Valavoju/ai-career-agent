function SkillsCard({ title, skills, color }) {
  return (
    <div className="skills-card">
      <h2>{title}</h2>

      <div className="skills-grid">
        {skills.map((skill) => (
          <span
            key={skill}
            className={`skill-chip ${color}`}
          >
            {skill}
          </span>
        ))}
      </div>
    </div>
  );
}

export default SkillsCard;