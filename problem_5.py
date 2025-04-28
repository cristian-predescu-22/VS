# Possible structure

def fizzbuzz(n):

    if not n or n == 0:
        return []

    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Test cases
print("--- Problem 5: FizzBuzz ---")
expected1 = ['1', '2', 'Fizz', '4', 'Buzz']
actual1 = fizzbuzz(5)
print(f"Input: 5, Expected: {expected1}, Actual: {actual1}")

expected2 = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
actual2 = fizzbuzz(15)
print(f"Input: 15, Expected: {expected2}, Actual: {actual2}")

expected3 = ['1', '2']
actual3 = fizzbuzz(2)
print(f"Input: 2, Expected: {expected3}, Actual: {actual3}")

expected4 = [] # Check edge case n=0
actual4 = fizzbuzz(0)
print(f"Input: 0, Expected: {expected4}, Actual: {actual4}")
print("-" * 20)