def calculate_score(request):
    score = (
        request.impact * 0.4 +
        request.urgency * 0.3 +
        request.customer_importance * 0.2 -
        request.effort * 0.1
    )
    return round(score, 2)