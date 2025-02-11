int_1 = int(input("What is the first number? "))
int_2 = int(input ("What is the second number? "))

if int_1 > int_2:
        print("The first number is greater")
else: 
        print("The first number is not greater")
     
           
if int_1 == int_2:
        print("The numbers are equal")
else:
        print("The numbers are not equal")
        

if int_1 > int_2:
         print("The second number is not greater")
elif int_1 == int_2:
        print("The second number is not greater")
else: 
        print("The second number is greater")
print()

animal = "eagle"
fav_ani = input("What is your favorite animal? ")
if fav_ani.lower() == animal:
        print("That's my favorite animal too!")
else:
        print("That one is not my favorite")