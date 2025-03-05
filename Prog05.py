#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

#Ask user for 2 numbers
print("Please Enter a number")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

remainder = num1 % num2             #Divide num1 by num2
print (remainder)                   #Print the remainder