# Simple Calculator in Python using input and if-else statements

# Taking input from the user for the first number
Number1 = float(input("Enter the first number: "))

# Taking input from the user for the second number
Number2 = float(input("Enter the second number: "))

# Asking the user to choose an operation
print("Choose an operation: +  -  *  /")
operation = input("Enter operation: ")

# Using if-elif-else to perform the selected operation
if operation == "+":
    result = Number1 + Number2
    print("The result is:", result)

elif operation == "-":
    result = Number1 - Number2
    print("The result is:", result)

elif operation == "*":
    result = Number1 * Number2
    print("The result is:", result)

elif operation == "/":
    # Check if the second number is not zero to avoid division error
    if Number2 != 0:
        result = Number1 / Number2
        print("The result is:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    # If the user enters an invalid operation
    print("Invalid operation selected.")
