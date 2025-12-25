
number = int(input("Enter a number: "))
sum = 0
for i in range(0, number + 1):
    sum = sum + i
    print(f"Adding {i}, current sum is: {sum}")
print(f"The sum of numbers from 1 to {number} is:", sum)