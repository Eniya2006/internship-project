class Request:
    def __init__(self, req_id, title, rtype, impact, urgency, effort, customer_importance):
        self.req_id = req_id
        self.title = title
        self.rtype = rtype
        self.impact = impact
        self.urgency = urgency
        self.effort = effort
        self.customer_importance = customer_importance
        self.score = 0

    def __repr__(self):
        return f"{self.req_id} - {self.title} | Score: {self.score}"
