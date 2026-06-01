def get_hiring_recommendation(score):

    if score >= 75:
        return {
            "recommendation": "Strong Hire",
            "confidence": 95
        }

    elif score >= 55:
        return {
            "recommendation": "Hire",
            "confidence": 85
        }

    elif score >= 30:
        return {
            "recommendation": "Borderline",
            "confidence": 75
        }

    else:
        return {
            "recommendation": "Needs Upskilling",
            "confidence": 70
        }