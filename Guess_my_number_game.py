import random
print("Welcome to the Guess My Number Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print()
replay = ""
while replay != "no":
    magic_number = random.randint(1, 100)
    #magic_number = int(input("What is the magic number? "))
    guess_number = 0
    counter = 0
    while guess_number != magic_number:   
        guess_number = int(input("What is your guess? "))
        counter += 1
        if guess_number < magic_number:
            print("Higher")
        elif guess_number > magic_number:
            print("Lower")
        else:
            print("You guessed it!")
            print(f"It took you, {counter} tries.")
            print()
            replay = str(input("Do you want to play again? (yes/no) "))
