# [classify_number.py]
# Author: [Obaid ur Rahman]
# Date: [29/09/2026]
# Description: [The script will take a number from user as input and display that the number is positive, negative or zero.]

# Get user input
number = int(input("Enter a number: "))


# Check condition
if number > 0:
    print(number, "is positive.")
elif number < 0:
    print(number, "is negative.")
else:
    print(number, "is zero.")
