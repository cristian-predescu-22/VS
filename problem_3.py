# Function definition (implement this)
def reverse_string(s):
    if not s:
        return ""
    reversed_list = []
    for i in range(-1, -len(s)-1, -1):
        reversed_list.append(s[i])
    return "".join(reversed_list)
    


# Test cases
print("--- Problem 3: Reverse String ---")
expected1 = "olleh"
actual1 = reverse_string("hello")
print(f"Input: 'hello', Expected: '{expected1}', Actual: '{actual1}'")

expected2 = "nohtyP"
actual2 = reverse_string("Python")
print(f"Input: 'Python', Expected: '{expected2}', Actual: '{actual2}'")

expected3 = ""
actual3 = reverse_string("")
print(f"Input: '', Expected: '{expected3}', Actual: '{actual3}'")

expected4 = "a"
actual4 = reverse_string("a")
print(f"Input: 'a', Expected: '{expected4}', Actual: '{actual4}'")
print("-" * 20)