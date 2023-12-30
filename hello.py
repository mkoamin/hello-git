def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(num)

# Print the result
print("The factorial of", num, "is", result)
