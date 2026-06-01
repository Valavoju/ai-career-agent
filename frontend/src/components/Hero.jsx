import { motion } from "framer-motion";

function Hero() {
  return (
    <motion.div
      className="hero"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.6 }}
    >
      <h1>AI Recruitment Gen Agents</h1>

      <p>
        Multi-Agent Recruitment Intelligence Platform
      </p>

      <div className="hero-features">

        <span>📄 Resume Screening Agent</span>

        <span>🧠 Skill Evaluation Agent</span>

        <span>📅 Interview Scheduling Agent</span>

        <span>🤖 Hiring Recommendation Agent</span>

        <span>📧 Candidate Communication Agent</span>

      </div>
    </motion.div>
  );
}

export default Hero;