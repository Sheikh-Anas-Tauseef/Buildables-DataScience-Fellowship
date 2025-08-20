#Task: Write a program that counts the number of vowels in a given string.

string = str(input('Enter a string: '))
vowels = "aeiosAEIOU"
count = sum(1 for char in string if char in vowels)

print("The number of vowels is: ",count)