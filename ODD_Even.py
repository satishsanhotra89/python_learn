
# to check the number is ODD or EVEN


try:
    for i in range(10):
        number = int(input("Enter a number to check if it is ODD or EVEN: "))
        if number % 2 == 0:
            print(f"{number} is an EVEN Number.")
        else:
            print(f"{number} is an ODD Number.")
except ValueError:
    print("Error: Invalid input. Please enter an integer value.")
 