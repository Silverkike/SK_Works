user_percentage = int(input("What is the student grade percentage? "))
remainder = user_percentage % 10

# Conditions to add to a grade letter a "+" or "-" or without sign 
if remainder >= 7:
    sign = "+"
elif remainder >= 3 or user_percentage == 100:
    sign =""
else:
    sign = "-"


if user_percentage >= 90:
    letter = "A"
    if remainder < 3 and not user_percentage >= 100:    # Condition to detect  if it's an A- or A
        sign = "-"
    else:
        sign = ""
elif user_percentage >= 80:
    letter = "B"
elif user_percentage >= 70:
    letter = "C"   
elif user_percentage >= 60:
    letter = "D"
elif user_percentage < 60:
    letter = "F"
    sign = ""



print(f"The Grade is: {letter}{sign}")

# Conditions to give or not a congratulation message since the passing grade is at least 70% 
if user_percentage >= 70:
    print("Congratulations to you for passing the course!")
else:
    print("We encourage you to strive more next time!")



