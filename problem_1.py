# Function definition (implement this)
def sum_list(numbers):
    total = 0
    if len(numbers) == 0:
        return 0
    else:
        for i in numbers:
            total += i
        return total




# Test cases
print("--- Problem 1: Sum of List ---")
expected1 = 6
actual1 = sum_list([1, 2, 3])
print(f"Input: [1, 2, 3], Expected: {expected1}, Actual: {actual1}")

expected2 = 0
actual2 = sum_list([-1, 0, 1])
print(f"Input: [-1, 0, 1], Expected: {expected2}, Actual: {actual2}")

expected3 = 0
actual3 = sum_list([])
print(f"Input: [], Expected: {expected3}, Actual: {actual3}")

expected4 = 12.5
actual4 = sum_list([10.5, 2.0])
print(f"Input: [10.5, 2.0], Expected: {expected4}, Actual: {actual4}")
print("-" * 20)