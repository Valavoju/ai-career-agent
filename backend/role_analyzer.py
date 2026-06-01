def get_role_requirements(role):

    roles = {

        "AI Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "Natural Language Processing",
            "Computer Vision",
            "Data Structures",
            "Cloud Computing",
            "DevOps",
            "API Design"
        ],

        "Machine Learning Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "Statistics",
            "Data Structures",
            "Cloud Computing"
        ],

        "Data Scientist": [
            "Python",
            "SQL",
            "Statistics",
            "Machine Learning",
            "Data Visualization",
            "Pandas",
            "NumPy"
        ],

        "Frontend Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Responsive Design",
            "Git"
        ],

        "Backend Developer": [
            "Python",
            "FastAPI",
            "Flask",
            "SQL",
            "REST API",
            "Git"
        ],

        "Full Stack Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Python",
            "SQL",
            "Git"
        ]
    }

    return {
        "required_skills": roles.get(role, [])
    }