# Function definition (implement this)
def first_non_repeating(text):
    count = {}
    for i in text:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i] + 1

    for x in text:
        if count[x] == 1:
            return x
    return None
        
# Test cases
print("--- Problem 10: First Non-Repeating Character ---")
expected1 = "l"
actual1 = first_non_repeating("leetcode")
print(f"Input: 'leetcode', Expected: '{expected1}', Actual: '{actual1}'")

expected2 = None
actual2 = first_non_repeating("aabbcc")
print(f"Input: 'aabbcc', Expected: {expected2}, Actual: {actual2}")

expected3 = "t"
actual3 = first_non_repeating("stress")
print(f"Input: 'stress', Expected: '{expected3}', Actual: '{actual3}'")

expected4 = "a"
actual4 = first_non_repeating("statistiques")
print(f"Input: 'statistiques', Expected: '{expected4}', Actual: '{actual4}'")

expected5 = "Z" # Case-sensitive
actual5 = first_non_repeating("ZzAa")
print(f"Input: 'ZzAa', Expected: '{expected5}', Actual: '{actual5}'")

expected6 = None
actual6 = first_non_repeating("")
print(f"Input: '', Expected: {expected6}, Actual: {actual6}")

expected7 = None # All repeating
actual7 = first_non_repeating("sss")
print(f"Input: 'sss', Expected: {expected7}, Actual: {actual7}")
print("-" * 20)