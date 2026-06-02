def generate_interview_plan(recommendation, score):

    if recommendation == "Strong Hire":

        return {
            "rounds": [
                "Technical Round",
                "Managerial Round",
                "HR Round"
            ],
            "slots": [
                "Tomorrow - 10:00 AM",
                "Tomorrow - 2:00 PM",
                "Next Working Day - 11:00 AM"
            ],
            "difficulty": "Advanced",
            "duration": "60 Minutes"
        }

    elif recommendation == "Hire":

        return {
            "rounds": [
                "Technical Round",
                "HR Round"
            ],
            "slots": [
                "Within 3 Days - 10:00 AM",
                "Within 3 Days - 2:00 PM"
            ],
            "difficulty": "Intermediate",
            "duration": "45 Minutes"
        }

    elif recommendation == "Borderline":

        return {
            "rounds": [
                "Skill Assessment",
                "Technical Round"
            ],
            "slots": [
                "Next Week - Monday 10:00 AM",
                "Next Week - Tuesday 11:00 AM"
            ],
            "difficulty": "Intermediate",
            "duration": "45 Minutes"
        }

    else:

        return {
            "rounds": [],
            "slots": [],
            "difficulty": "N/A",
            "duration": "N/A",
            "message":
                "Candidate requires additional upskilling before interview scheduling."
        }