#if marks <=60 then Student is pass else fail
#if marks>60 then check for grade
#>=90 then grade A
#>=80-89 then grade B
#>=70-79 then grade C
#>=60-69 then grade D


for i in range(5):
    def pass_fail(marks):
        if marks < 60:
            return "Fail"
        elif marks >= 90:
            return "Pass with Grade A"
        elif marks >= 80 and marks <= 89:
            return "Pass with Grade B"
        elif marks >= 70 and marks <= 79:
            return "Pass with Grade C"
        elif marks >= 60 and marks <= 69:
            return "Pass with Grade D"

    # Get input from user
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            result = pass_fail(marks)
            print(f"Marks: {marks}, Result: {result}")
        else:
            print("Please enter marks between 0 and 100")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

