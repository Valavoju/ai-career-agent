import { motion } from "framer-motion";

function Hero() {
  return (
    <motion.div
      className="hero"
      initial={{ opacity: 0, y: -30 }}
      animate={{ opacity: 1, y: 0 }}
    >
      <h1>AI Career Research Agent</h1>
      <p>
        Upload your resume, discover skill gaps,
        and get an AI-powered career roadmap.
      </p>
    </motion.div>
  );
}

export default Hero;