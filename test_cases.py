
from models import Request
from scorer import calculate_score

def test_score_positive():
    req = Request(1, "Test", "bug", 5, 5, 1, 5)
    score = calculate_score(req)
    assert score > 0
    print("Test 1 Passed")

def test_score_comparison():
    r1 = Request(1, "High Impact", "feature", 5, 5, 2, 5)
    r2 = Request(2, "Low Impact", "feature", 2, 2, 2, 2)

    assert calculate_score(r1) > calculate_score(r2)
    print("Test 2 Passed")

test_score_positive()
test_score_comparison()
