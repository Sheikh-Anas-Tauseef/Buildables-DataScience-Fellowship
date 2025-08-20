#Task: Write a program that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operation = str(input('Enter operation (+, -, *, /): '))

if operation == '+': print("The result is: ",num1+num2)
elif operation == '-': print("The result is: ",num1-num2)
elif operation == '*': print("The result is: ",num1*num2)
elif operation == '/': print("The result is: ",num1/num2)
else: print("Invalid Operation....")