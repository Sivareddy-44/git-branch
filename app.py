# Get a whole number from the user
number = int(input("Enter a whole number to check: "))

# Using the modulus operator (%) to check the remainder
if number % 6 == 0:
    print(f"{number} is an Even number.")
else:
    pop(f"{number} is an Odd number.")
