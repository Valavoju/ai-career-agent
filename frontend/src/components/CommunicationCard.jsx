import emailjs from "@emailjs/browser";

function CommunicationCard({ result }) {

  const sendEmail = () => {

    if (!result.candidate_email) {
  alert(
    "No email address found in the uploaded resume."
  );
  return;
}

   emailjs.send(
  "service_y2xmyd4",
  "template_fecm0dj",
  {
    candidate_name: result.candidate_name,

    to_email: result.candidate_email,

    role: result.role,

    score: result.match_score,

    recommendation: result.recommendation,

    confidence: result.confidence,

    matching_skills:
      result.matching_skills.join(", "),

    missing_skills:
      result.missing_skills.join(", "),

    roadmap: result.roadmap,
  },
  "kYNRgwz1CN6SWMunc"
)
    .then(() => {
      alert("Email sent successfully!");
    })
    .catch((error) => {
  console.error("EmailJS Error:", error);

  alert(
    JSON.stringify(error)
  );
});
  };

  return (
    <div className="dashboard-card communication-card">

      <h2>📧 Candidate Communication Agent</h2>

      <div className="email-content">

        <p>
          Click below to send the complete
          recruitment report to your email.
        </p>

      </div>

      <button
        className="analyze-btn"
        onClick={sendEmail}
      >
        📨 Send Report to Email
      </button>

    </div>
  );
}

export default CommunicationCard;