import math

while True:
    try:
        value = int(input("Enter a number for Square_root and Log value: "))
        def calculate_sqrt_log(value):
            if value < 0:
                raise ValueError("Cannot compute square root of a negative number.")
            sqrt_value = math.sqrt(value)
            log_value = math.log(value) if value > 0 else float('-inf')
            sin_value = math.sin(value) if value > 0 else float('-inf')
            return sqrt_value, log_value, sin_value
        print(f"square root of {value} is {calculate_sqrt_log(value)[0]}")
        print(f"natural log of {value} is {calculate_sqrt_log(value)[1]}")
        print(f"natural log of {value} is {calculate_sqrt_log(value)[2]}")
    except ValueError as ve:
        print(f"Error: {ve}")
    choice = input("Do you want to calculate Square_root and Log value again? (yes/no): ").lower()
    if choice != 'yes':
        print("Exiting the Square_root and Log calculator. Goodbye!")
        break