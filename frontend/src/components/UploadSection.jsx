import { motion } from "framer-motion";

function UploadSection({
  file,
  setFile,
  role,
  setRole,
  roles,
  analyzeResume,
  loading,
}) {
  return (
    <motion.div
      className="upload-card"
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2>📄 Candidate Resume Upload</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <h2>💼 Job Position</h2>

      <select
        value={role}
        onChange={(e) => setRole(e.target.value)}
      >
        {roles.map((r) => (
          <option key={r}>{r}</option>
        ))}
      </select>

      <button
        className="analyze-btn"
        onClick={analyzeResume}
      >
        {loading ? "Analyzing..." : "🤖 Start Recruitment Analysis"}
      </button>
    </motion.div>
  );
}

export default UploadSection;