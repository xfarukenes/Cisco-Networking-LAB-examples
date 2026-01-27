# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)


print("----- Alternative Implementation -----")

# Read three numbers
number4 = int(input("Enter the first number: "))
number5 = int(input("Enter the second number: "))
number6 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number4

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number5 > largest_number:
    largest_number = number5

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number6 > largest_number:
    largest_number = number6

# Print the result
print("The largest number is:", largest_number)

