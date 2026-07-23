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