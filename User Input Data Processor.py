#Task 1: Input Length Validator: Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

first_name_length = len(first_name)
last_name_length = len(last_name)

if first_name_length < 2:
    print("Error. Please enter name again.")
if last_name_length <2:
    print("Error. Please enter name again.")
else:
    print("Thank you for the information.")    