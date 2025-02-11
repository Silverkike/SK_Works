# I have lengthened the story adding some extra variables, those are: place, person's name, food and object. With these new additions, the story becomes richer and more detailed. 
print("Please enter the following")
print()

# Here we gather the user' data.
adjective = input("An Adjective: ")
animal = input("An Animal: ")
verb1 = input("A Verb: ")
exclamation = input("An Exclamation: ")
verb2 = input("Another Verb: ")
verb3 = input("Another Verb again: ")
place = input("A Place: ")
person_name = input("A Person's name: ")
food = input("A Type of Food: ")
object = input("An Object: ")

print()

# Here the story is created with the words inputted by user.
print("Your story is: ")
print()
print(f"The other day, I was really in trouble. It all started when I saw a very")
print(adjective + " " +  animal + " " + verb1 + " " + "down the hallway." + '"' + exclamation.capitalize() + '!"' + " " + "I yelled. But all")
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3} ")
print(f"right in front of my family. We ran to {place.title()}, where we met")
print(f"{person_name.title()}, who was enjoying some {food}. After a brief chat, {person_name.title()} handed me a {object} and said it would")
print(f"help me if I ever encountered a {adjective} {animal} again.")
# End of Program.
# Author: Carlos Enrique Guardado Cruz.