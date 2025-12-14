

num1= input("Enter your first number:")
num2= input("Enter your second number:")

try:
    num1=int(num1)
    num2=int(num2)
    print("The addition of two numbers is:", num1 + num2)
    print("The subtraction of two numbers is:", num1 - num2)
    print("The multiplication of two numbers is:", num1 * num2)
    print("The division of two numbers is:", num1 / num2)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
