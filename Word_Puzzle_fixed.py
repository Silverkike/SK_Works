# I have added a list of random words to guess from. Then the program will randomly choose one of the words to guess.
# Author: Carlos Enrique Guardado Cruz.

import random

print("Welcome to word guessing game!")
print()
palabras = ["apple", "elderberry", "mosiah", "alma", "nephi", "temple", "church", "jesus", "god", "atonement"]
secret_word = random.choice(palabras)

# Initialize the result list with underscores
resultado = ["_"] * len(secret_word)

# Give the first hint
print("Your hint is: ", " ".join(resultado))

# Ask for the guess
guess = ""
counter = 0
while guess != secret_word:
    print()
    guess = input("What is your guess? ")
    counter += 1
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word. Try again!.")
    else:
        resultado = []
        for i in range(len(secret_word)):      # This part compares the guess with the secret word letter by letter
            if guess[i] == secret_word[i]:
                resultado.append(guess[i].upper())
            elif guess[i] in secret_word:
                resultado.append(guess[i].lower())
            else:
                resultado.append("_")

        print(" ".join(resultado))

print("Congratulations! You guessed it!")
print(f"It took you, {counter} guesses.")
# End of the program
           




