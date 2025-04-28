def is_palindrome(s):
    if not s:
        return True

    processed_s = s.lower() # Ignore case

    left = 0
    right = len(processed_s) - 1
    for _ in range(len(processed_s)):
        if processed_s[left] == processed_s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# TO DO ---------------------
# Make this task with While loop because
# Left and Right pointer only need to meet
# Not go all the way around
# while left < right


# Test cases
print("--- Problem 4: Check Palindrome ---")
expected1 = True
actual1 = is_palindrome("Racecar")
print(f"Input: 'Racecar', Expected: {expected1}, Actual: {actual1}")

expected2 = False
actual2 = is_palindrome("hello")
print(f"Input: 'hello', Expected: {expected2}, Actual: {actual2}")

expected3 = True
actual3 = is_palindrome("level")
print(f"Input: 'level', Expected: {expected3}, Actual: {actual3}")

expected4 = True # Testing case insensitivity
actual4 = is_palindrome("Madam")
print(f"Input: 'Madam', Expected: {expected4}, Actual: {actual4}")

expected5 = True
actual5 = is_palindrome("a")
print(f"Input: 'a', Expected: {expected5}, Actual: {actual5}")

expected6 = True
actual6 = is_palindrome("")
print(f"Input: '', Expected: {expected6}, Actual: {actual6}")
print("-" * 20)