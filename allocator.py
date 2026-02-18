
from scorer import calculate_score

def prioritize_requests(request_list):
    for req in request_list:
        req.score = calculate_score(req)

    sorted_list = sorted(request_list, key=lambda x: x.score, reverse=True)
    return sorted_list


def allocate_resources(sorted_requests, max_capacity):
    allocated = []
    used_capacity = 0

    for req in sorted_requests:
        if used_capacity + req.effort <= max_capacity:
            allocated.append(req)
            used_capacity += req.effort

    return allocated
