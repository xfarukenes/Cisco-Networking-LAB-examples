# Initialize counters and lists.
odd_numbers = 0
even_numbers = 0

list_of_odd_numbers = []
list_of_even_numbers = []

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
        list_of_odd_numbers.append(number)
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
        list_of_even_numbers.append(number)
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers, "->", list_of_odd_numbers)
print("Even numbers count:", even_numbers, "->", list_of_even_numbers)