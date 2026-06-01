def generate_roadmap(role, missing_skills):

    if not missing_skills:
        return f"""
# Congratulations 🎉

You already match most requirements for the {role} role.

Continue building projects, practicing interview questions, and improving system design skills.
"""

    roadmap = f"# Learning Roadmap: {role}\n\n"

    roadmap += "## Phase 1: Foundations (3-6 months)\n"

    for skill in missing_skills[:3]:
        roadmap += f"- Learn {skill}\n"

    roadmap += "\n## Phase 2: Specialized Topics (6-12 months)\n"

    for skill in missing_skills[3:6]:
        roadmap += f"- Gain hands-on experience in {skill}\n"

    roadmap += "\n## Phase 3: Projects and Practice\n"
    roadmap += "- Build real-world projects\n"
    roadmap += "- Participate in hackathons\n"
    roadmap += "- Practice technical interviews\n"

    return roadmap