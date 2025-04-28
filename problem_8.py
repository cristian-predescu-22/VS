# Function definition (implement this)
def merge_sorted_lists(list1, list2):
    if not list1 and not list2:
        return []
    
    left = 0
    right = 0
    sorted_list = []
    while left < len(list1) or right < len(list2):
        if left >= len(list1):
            sorted_list.append(list2[right])
            right += 1
        elif right >= len(list2):
            sorted_list.append(list1[left])
            left += 1
        else:
            if list1[left] < list2[right]:
                sorted_list.append(list1[left])
                left += 1
            else:
                sorted_list.append(list2[right])
                right += 1

        
    return sorted_list

# Test cases
print("--- Problem 8: Merge Sorted Lists ---")
expected1 = [1, 2, 3, 4, 5, 6]
actual1 = merge_sorted_lists([1, 3, 5], [2, 4, 6])
print(f"Input: ([1, 3, 5], [2, 4, 6]), Expected: {expected1}, Actual: {actual1}")

expected2 = [1, 2, 3, 4, 5, 6]
actual2 = merge_sorted_lists([1, 2, 3], [4, 5, 6])
print(f"Input: ([1, 2, 3], [4, 5, 6]), Expected: {expected2}, Actual: {actual2}")

expected3 = [1, 2, 3, 4, 8, 9]
actual3 = merge_sorted_lists([1, 4, 8], [2, 3, 9])
print(f"Input: ([1, 4, 8], [2, 3, 9]), Expected: {expected3}, Actual: {actual3}")

expected4 = [1, 5, 10]
actual4 = merge_sorted_lists([10], [1, 5])
print(f"Input: ([10], [1, 5]), Expected: {expected4}, Actual: {actual4}")

expected5 = [2, 4]
actual5 = merge_sorted_lists([], [2, 4])
print(f"Input: ([], [2, 4]), Expected: {expected5}, Actual: {actual5}")

expected6 = [1, 3]
actual6 = merge_sorted_lists([1, 3], [])
print(f"Input: ([1, 3], []), Expected: {expected6}, Actual: {actual6}")

expected7 = []
actual7 = merge_sorted_lists([], [])
print(f"Input: ([], []), Expected: {expected7}, Actual: {actual7}")
print("-" * 20)