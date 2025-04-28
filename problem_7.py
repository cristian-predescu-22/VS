# Function definition (implement this)
def get_evens(numbers):
    if not numbers:
        return []
    
    new_list = []
    for i in numbers:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

# Test cases
print("--- Problem 7: Get Even Numbers ---")
expected1 = [2, 4, 6]
actual1 = get_evens([1, 2, 3, 4, 5, 6])
print(f"Input: [1, 2, 3, 4, 5, 6], Expected: {expected1}, Actual: {actual1}")

expected2 = [10, 0, -2]
actual2 = get_evens([10, 0, -2, 1, 3, 5])
print(f"Input: [10, 0, -2, 1, 3, 5], Expected: {expected2}, Actual: {actual2}")

expected3 = []
actual3 = get_evens([1, 3, 5])
print(f"Input: [1, 3, 5], Expected: {expected3}, Actual: {actual3}")

expected4 = []
actual4 = get_evens([])
print(f"Input: [], Expected: {expected4}, Actual: {actual4}")
print("-" * 20)