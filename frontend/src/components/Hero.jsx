import { motion } from "framer-motion";

function Hero() {
  return (
    <motion.div
      className="hero"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      <h1>CareerPilot AI</h1>

      <p>
        Your Personal AI Career Strategist
      </p>

      <div className="hero-features">
        <span>✓ ATS Resume Analysis</span>
        <span>✓ Skill Gap Detection</span>
        <span>✓ AI Career Roadmap</span>
        <span>✓ 13+ Job Roles</span>
      </div>
    </motion.div>
  );
}

export default Hero;