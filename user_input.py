'''
Write a program that asks the user for their name, age, and location and then prints out a personalized message.




Instructions:
Create a new Python file and name it "user_input.py"
Use the input() function to ask the user for their name and store it in a variable called "name".
Use the input() function to ask the user for their age and store it in a variable called "age".
Use the input() function to ask the user for their location and store it in a variable called "location".
Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
Save and run the program to see the output.
'''

name = input("What is your name? ")
age = input("How old are you? ")
location = input("What is your location? ")
print("Hello {}, you are {} years old and live in {}".format(name, age, location))
