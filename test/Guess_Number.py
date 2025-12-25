correct_num=19
try:
    #import random
    #correct_num=random.randint(1,100)
    for i in range (0,10,1):
        try:
            user_input=int(input("Guess and Enter a number between 1 to 100: "))
            if user_input < correct_num:
                print("Your guess is too low, try again.")
            elif user_input > correct_num:
                print("Your guess is too high, try again.")
            else:
                print("Congratulations! You guessed the correct number.")
                break  # Exit the loop on correct guess
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    else:
        print("Sorry, you've used all your attempts. The correct number was", correct_num)
except:
    pass