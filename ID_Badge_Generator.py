"""
This program gathers personal information from the user and then displays or create an ID Badge like a Driver License.
Author: SILVERKIKE
"""

# The program starts to gather information
print("Please enter de following information:")
print()
first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email address: ")
phone = input("Phone Number: ")
job =  input("Job Title: ")
id_number = input("ID Number: ")
hair = input("Hair Color: ")
eyes = input("Eyes Color: ")
month = input("Driving starting Month: ")
training = input("Do you have any previously driving training (yes/no)? ")

# The program arranges the data gathered from user and displays it properly and formatted as it was asked for.
print()
print("The ID Card is:")
print("------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair: {hair.capitalize()}     Eyes: {eyes.capitalize()}")
print(f"Month: {month.capitalize()}   Training: {training.capitalize()}")
print("------------------------------------")