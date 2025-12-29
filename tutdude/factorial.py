
while True:
    def fact (num):
        if num==0 or num==1:
            return 1
        else:
            return num*fact(num-1)
    try: 
        number=int(input("Enter a number to find factorial: "))
        result=fact(number)
        print(f"The factorial of {number} is {result}")
    except ValueError:
        print("Please enter a valid integer.")
    choice=input("Do you want to calculate another factorial? (yes/no): ").lower()
    if choice != 'yes':
        print("Exiting the factorial calculator. Goodbye!")
        break
    