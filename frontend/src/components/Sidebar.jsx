function Sidebar({ activeTab, setActiveTab }) {
  return (
    <div className="sidebar">
      <div className="sidebar-logo">RecruitAI</div>

      <ul className="sidebar-menu">
        <li
          className={activeTab === "dashboard" ? "active" : ""}
          onClick={() => setActiveTab("dashboard")}
        >
          🏠 Dashboard
        </li>

        <li
          className={activeTab === "screening" ? "active" : ""}
          onClick={() => setActiveTab("screening")}
        >
          📄 Resume Screening
        </li>

        <li
          className={activeTab === "skills" ? "active" : ""}
          onClick={() => setActiveTab("skills")}
        >
          🧠 Skill Evaluation
        </li>

        <li
          className={activeTab === "interview" ? "active" : ""}
          onClick={() => setActiveTab("interview")}
        >
          📅 Interview Planner
        </li>

        <li
          className={activeTab === "hiring" ? "active" : ""}
          onClick={() => setActiveTab("hiring")}
        >
          🤖 Hiring Decision
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
