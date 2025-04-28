# Function definition (implement this)
def factorial(n):
    if n == 1 or n == 0:
        return 1
    total = 1
    for i in range(1, n):
        total += total * i
    return total

# Test cases
print("--- Problem 9: Factorial ---")
expected1 = 120
actual1 = factorial(5)
print(f"Input: 5, Expected: {expected1}, Actual: {actual1}")

expected2 = 6
actual2 = factorial(3)
print(f"Input: 3, Expected: {expected2}, Actual: {actual2}")

expected3 = 1
actual3 = factorial(1)
print(f"Input: 1, Expected: {expected3}, Actual: {actual3}")

expected4 = 1
actual4 = factorial(0)
print(f"Input: 0, Expected: {expected4}, Actual: {actual4}")

# Optional: How should it handle negative numbers? Returning None, 0, or raising error are options.
# expected5 = None # Example if deciding to return None for negatives
# actual5 = factorial(-5)
# print(f"Input: -5, Expected: {expected5}, Actual: {actual5}")
print("-" * 20)