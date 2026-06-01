function Sidebar({
  activeTab,
  setActiveTab,
}) {
  return (
    <div className="sidebar">

      <div className="sidebar-logo">
        RecruitAI
      </div>

      <ul className="sidebar-menu">

        <li
          className={
            activeTab === "dashboard"
              ? "active"
              : ""
          }
          onClick={() =>
            setActiveTab("dashboard")
          }
        >
          🏠 Dashboard
        </li>

        <li
          className={
            activeTab === "screening"
              ? "active"
              : ""
          }
          onClick={() =>
            setActiveTab("screening")
          }
        >
          📄 Screening
        </li>

        <li
          className={
            activeTab === "skills"
              ? "active"
              : ""
          }
          onClick={() =>
            setActiveTab("skills")
          }
        >
          🧠 Skills
        </li>

        <li
          className={
            activeTab === "interview"
              ? "active"
              : ""
          }
          onClick={() =>
            setActiveTab("interview")
          }
        >
          📅 Interview
        </li>

        <li
          className={
            activeTab === "communication"
              ? "active"
              : ""
          }
          onClick={() =>
            setActiveTab("communication")
          }
        >
          📧 Communication
        </li>

        <li
          className={
            activeTab === "recommendation"
              ? "active"
              : ""
          }
          onClick={() =>
            setActiveTab("recommendation")
          }
        >
          🤖 Hiring
        </li>

      </ul>

    </div>
  );
}

export default Sidebar;