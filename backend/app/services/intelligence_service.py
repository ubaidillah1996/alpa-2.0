def generate_project_insight(
    summary: dict
):

    insights = []
    recommendations = []


    progress = summary["progress"]
    high_priority = summary["high_priority_tasks"]
    pending_tasks = summary["pending_tasks"]


    if progress < 50:
        insights.append(
            "Project progress is below 50%"
        )

        recommendations.append(
            "Focus on completing pending tasks first"
        )


    if high_priority > 0:
        insights.append(
            f"There are {high_priority} high priority tasks remaining"
        )

        recommendations.append(
            "Prioritize high impact tasks"
        )


    if pending_tasks == 0:
        insights.append(
            "All tasks are completed"
        )

        recommendations.append(
            "Review project outcome and plan next milestone"
        )


    if not insights:
        insights.append(
            "Project is progressing well"
        )

        recommendations.append(
            "Continue current workflow"
        )


    return {
        "status": "generated",
        "insights": insights,
        "recommendations": recommendations
    }

def calculate_productivity_score(
    summary: dict
):

    progress = summary["progress"]

    high_priority = summary["high_priority_tasks"]

    pending_tasks = summary["pending_tasks"]


    score = 0


    # Completion contribution
    score += progress * 0.5


    # Priority contribution
    if high_priority == 0:
        score += 30

    elif high_priority <= 2:
        score += 20

    else:
        score += 10


    # Pending workload contribution
    if pending_tasks <= 2:
        score += 20

    elif pending_tasks <= 5:
        score += 10

    else:
        score += 5


    score = round(score)


    if score >= 80:
        level = "Excellent"

    elif score >= 60:
        level = "Good"

    elif score >= 40:
        level = "Needs Attention"

    else:
        level = "Critical"


    return {
        "productivity_score": score,
        "level": level
    }