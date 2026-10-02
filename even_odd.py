# [even_odd.py]
# Author: [Obaid ur Rahman]
# Date: [29/09/2026]
# Description: [The script will take a number from user as input and display that the number is even or odd.]

# Get user input
number = int(input("Enter a number: "))


# Check condition
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
