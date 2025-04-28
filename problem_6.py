# Function definition (implement this)
def count_char(text, char_to_find):
    if not text:
        return 0
    
    total = 0
    for i in text:
        if i == char_to_find:
            total+=1
    return total


# Test cases
print("--- Problem 6: Count Character ---")
expected1 = 3
actual1 = count_char("Hello World", "l")
print(f"Input: ('Hello World', 'l'), Expected: {expected1}, Actual: {actual1}")

expected2 = 2
actual2 = count_char("Programming", "m")
print(f"Input: ('Programming', 'm'), Expected: {expected2}, Actual: {actual2}")

expected3 = 2 # Case-sensitive
actual3 = count_char("Success", "s")
print(f"Input: ('Success', 's'), Expected: {expected3}, Actual: {actual3}")

expected4 = 0
actual4 = count_char("Test", "z")
print(f"Input: ('Test', 'z'), Expected: {expected4}, Actual: {actual4}")

expected5 = 0
actual5 = count_char("", "a")
print(f"Input: ('', 'a'), Expected: {expected5}, Actual: {actual5}")
print("-" * 20)