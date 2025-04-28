# Function definition (implement this)
def find_max(numbers):
    # Handle empty list case (optional for now, good practice later)
    if not numbers:
        return None # Or decide on appropriate return value for empty list
    maximum = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum


# Test cases
print("--- Problem 2: Find Max ---")
expected1 = 9
actual1 = find_max([1, 5, 2, 9, 3])
print(f"Input: [1, 5, 2, 9, 3], Expected: {expected1}, Actual: {actual1}")

expected2 = -2
actual2 = find_max([-10, -5, -2, -9])
print(f"Input: [-10, -5, -2, -9], Expected: {expected2}, Actual: {actual2}")

expected3 = 42
actual3 = find_max([42])
print(f"Input: [42], Expected: {expected3}, Actual: {actual3}")

# Optional: Test empty list case if you implemented it
# expected4 = None # Or your chosen return value for empty lists
# actual4 = find_max([])
# print(f"Input: [], Expected: {expected4}, Actual: {actual4}")
print("-" * 20)