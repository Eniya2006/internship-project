from models import Request
from allocator import prioritize_requests, allocate_resources

# Sample data
requests = [
    Request(1, "Fix Payment Bug", "bug", 5, 5, 2, 5),
    Request(2, "Add Analytics Feature", "feature", 4, 3, 4, 4),
    Request(3, "Refactor Legacy Code", "tech_debt", 3, 2, 5, 2),
    Request(4, "VIP Client Customization", "customer", 5, 4, 3, 5),
]

# Step 1: Prioritize
sorted_requests = prioritize_requests(requests)

print("\n--- Prioritized Requests ---")
for r in sorted_requests:
    print(r)

# Step 2: Allocate based on limited capacity (example: total effort limit = 7)
allocated = allocate_resources(sorted_requests, max_capacity=7)

print("\n--- Allocated Tasks (Capacity = 7) ---")
for r in allocated:
    print(r)