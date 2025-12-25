def check_grade(marks):
    """
    Determine grade based on marks (0-100)
    """
    if marks >= 90:
        return 'Grade_A'
    elif marks >= 80:
        return 'Grade_B'
    elif marks >= 70:
        return 'Grade_C'
    elif marks >= 60:
        return 'Grade_D'
    elif marks >= 50:
        return 'Grade_E'
    else:
        return 'Grade_F'


# Get input from user
try:
    marks = float(input("Enter marks (0-100): "))
    if 0 <= marks <= 100:
        grade = check_grade(marks)
        print(f"Marks: {marks}, {grade}")
    else:
        print("Please enter marks between 0 and 100")
except ValueError:
    print("Invalid input. Please enter a numeric value")