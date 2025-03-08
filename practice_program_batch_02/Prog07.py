#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

#Ask user for 10 numbers
count = 0

for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    if num % 2 == 0:                #Check even numbers
        count += 1
print (count)                       #Print the number of even numbers