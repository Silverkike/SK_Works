# I have added a hidden path that the player can unlock by choosing the glowing book and only for the first book they choose. I shared the game with two friends and say the game was enjoyable, with a charming and nostalgic feel reminiscent of classic text adventures.
# Author: Carlos Enrique Guardado Cruz.
import sys

hidden_path = False

print("You've just inherited the Enchanted Library. As you step inside, the air is filled with a mysterious glow.")
print("On the central table, three books lay open:")
print()

while True:
        print("* ANCIENT GRIMOIRE OF SPELLS: Promises knowledge of powerful magic.")
        print("* DRAGON'S LAIR: Adventures in a land filled with dragons and treasures.")
        print("* LOST CITY OF ATLANTIS: Uncover secrets of the legendary underwater city.")
        print("You notice a faint glow coming from a closed book on a nearby shelf. It feels out of place.")
    
        user_choice_1 = str(input("Wich one will you read first? (or investigate the glowing book) "))
        print()

        if user_choice_1.lower() == "ancient grimoire of spells":
            while True:
                print("As you delve into the grimoire, you come across a spell that can grant you a single wish. However, the spell is written in a cryptic language. What will you do next?")
                print("* TRY TO DECODE THE SPELL YOURSELF")
                print("* SEARCH FOR A MAGICAL CREATURE TO HELP")

                user_choice_2 = str(input("What will you do next? "))
                print()            

                if user_choice_2.lower() == "try to decode the spell yourself":
                    while True:
                        print("You struggle with the cryptic text, but manage to decipher part of it. The spell requires a rare ingredient. Will you:")
                        print("* SEARCH THE LIBRARY FOR THE INGREDIENT")
                        print("* VENTURE INTO A MAGICAL FOREST TO FIND IT")

                        user_choice_3 = str(input("What will you do next? "))
                        print()

                        if user_choice_3.lower() == "search the library for the ingredient":
                            print("You find the ingredient hidden in a dusty corner of the library. The spell is now complete and you have inmortality. Congratulations!")
                            if hidden_path:
                                print("You also find a secret path that leads to a hidden chamber filled with treasures. You are now the master of the Enchanted Library. Congratulations!")                      
                            sys.exit("You have completed your adventure. GAME OVER!")
                        elif user_choice_3.lower() == "venture into a magical forest to find it":
                            print("You venture into the forest and find the rare ingredient, but you are ambushed by dark creatures and barely escape with your life. The spell is now complete and you have the power to fly. Congratulations!")
                            if hidden_path:
                                print("You also find a secret path that leads to a hidden chamber filled with treasures. You are now the master of the Enchanted Library. Congratulations!")                     
                            sys.exit("You have completed your adventure. GAME OVER!")
                        else:
                            print("You've chosen the wrong path! Try again.")
                            print()
                elif user_choice_2.lower() == "search for a magical creature to help":
                    while True:
                        print("You find a mischievous fairy willing to assist you, but she demands a favor in return. Will you:")
                        print("* AGREE TO HER TERMS")
                        print("* TRICK HER INTO HELPING YOU WITHOUT FULFILLING THE FAVOR")

                        user_choice_3 = str(input("What will you do next? "))
                        print()

                        if user_choice_3.lower() == "agree to her terms":
                            print("The fairy helps you decode the spell and grants your wish. You now have the power to control time. Congratulations!")
                            if hidden_path:
                                print("You also find a secret path that leads to a hidden chamber filled with treasures. You are now the master of the Enchanted Library. Congratulations!")                     
                            sys.exit("You have completed your adventure. GAME OVER!")
                        elif user_choice_3.lower() == "trick her into helping you without fulfilling the favor":
                            print("The fairy sees through your trickery and curses you with bad luck. You barely escape with your life. The spell is now complete and you have the power to control the elements. Congratulations!")
                            if hidden_path:
                                print("You also find a secret path that leads to a hidden chamber filled with treasures. You are now the master of the Enchanted Library. Congratulations!")                     
                            sys.exit("You have completed your adventure. GAME OVER!")     
                        else:
                            print("You've chosen the wrong path! Try again.")
                            print()
                else:
                    print("You've chosen the wrong path! Try again.")
                    print()
        elif user_choice_1.lower() == "glowing book":
            print("You open the glowing book and are transported to a mysterious realm of infinite possibilities!")
            print("You now have access to secret paths in your adventure.")
            print("You return to the central table and the three books lay open:")
            print()
            hidden_path = True
        elif user_choice_1.lower() == "dragon's lair":
            while True:
                print("You find yourself in a cavern filled with glittering jewels and an enormous sleeping dragon. Suddenly, the dragon stirs. What will you do?")
                print("* TIPTOE PAST THE DRAGON TO GET THE TREASURE")
                print("* WAKE THE DRAGON AND ASK FOR ITS BLESSING")

                user_choice_2 = str(input("What will you do next? "))
                print()

                if user_choice_2.lower() == "tiptoe past the dragon to get the treasure":
                    while True:
                        print("You reach the treasure, but a magical guardian appears. Will you:")
                        print("* FIGHT THE GUARDIAN")
                        print("* OFFER THE GUARDIAN A TRADE")

                        user_choice_3 = str(input("What will you do next? "))
                        print()

                        if user_choice_3.lower() == "fight the guardian":
                            print("You defeat the guardian and claim the treasure. The dragon awakens and offers you its blessing. You now have the power to shapeshift. Congratulations!")                     
                            sys.exit("You have completed your adventure. GAME OVER!")
                        elif user_choice_3.lower() == "offer the guardian a trade":
                            print("The guardian accepts your offer and lets you take the treasure. The dragon awakens and offers you its blessing. You now have the power to breathe underwater. Congratulations!")                     
                            sys.exit("You have completed your adventure. GAME OVER!")
                        else:
                            print("You've chosen the wrong path! Try again.")
                            print()
                elif user_choice_2.lower() == "wake the dragon and ask for its blessing":
                    while True:
                        print("The dragon, initially irate, listens to your request. It demands an ancient relic in return. Will you:")
                        print("* SEARCH THE CAVERN FOR THE RELIC")
                        print("* PROMISE TO BRING THE RELIC LATER")

                        user_choice_3 = str(input("What will you do next? "))
                        print()

                        if user_choice_3.lower() == "search the cavern for the relic":
                            print("You find the relic hidden in a crevice. The dragon grants you its blessing and you now have the power to control fire. Congratulations!")                     
                            sys.exit("You have completed your adventure. GAME OVER!")
                        elif user_choice_3.lower() == "promise to bring the relic later":
                            print("The dragon is skeptical, but agrees to wait. You leave the cavern and embark on a quest to find the relic. The dragon's blessing awaits you. Congratulations!")                     
                            sys.exit("You have completed your adventure. GAME OVER!")
                        else:
                            print("You've chosen the wrong path! Try again.")
                            print()
                else:
                    print("You've chosen the wrong path! Try again.")
                    print()           
        elif user_choice_1.lower() == "lost city of atlantis":
            while True:
                print("Upon arriving in Atlantis, you are greeted by its inhabitants who need your help. There is a powerful artifact that must be retrieved to save their city from doom. What’s your move?")
                print("* SWIM TO THE SUNKEN TEMPLE")
                print("* CONSULT WITH THE ATLANTEAN WISE ONES")
                print("* SEARCH FOR A MAP OF THE CITY")

                user_choice_2 = str(input("What will you do next? "))
                print()

                if user_choice_2.lower() == "swim to the sunken temple":
                    while True:
                        print("You face a series of underwater traps. Will you:")
                        print("* USE YOUR AGILITY TO NAVIGATE THE TRAPS")
                        print("* SEARCH FOR ANCIENT ATLANTEAN BLUEPRINTS TO DISARM THEM")

                        user_choice_3 = str(input("What will you do next? "))
                        print()

                        if user_choice_3.lower() == "use your agility to navigate the traps":
                            print("You narrowly avoid the traps and reach the artifact. The Atlanteans are grateful and grant you the power to breathe underwater. Congratulations!")
                            sys.exit("You have completed your adventure. GAME OVER!")
                        elif user_choice_3.lower() == "search for ancient atlantean blueprints to disarm them":
                            print("You find the blueprints and disarm the traps. The Atlanteans are grateful and grant you the power to control water. Congratulations!")
                            sys.exit("You have completed your adventure. GAME OVER!")
                        else:
                            print("You've chosen the wrong path! Try again.")
                            print()
                elif user_choice_2.lower() == "consult with the atlantean wise ones":
                    while True:
                        print("They reveal a prophecy that might help. Will you:")
                        print("* FOLLOW THE PROPHECY TO THE LETTER")
                        print("* INTERPRET THE PROPHECY YOUR OWN WAY")

                        user_choice_3 = str(input("What will you do next? "))
                        print()

                        if user_choice_3.lower() == "follow the prophecy to the letter":
                            print("You follow the prophecy and find the artifact. The Atlanteans are grateful and grant you the power to control the tides. Congratulations!")
                            sys.exit("You have completed your adventure. GAME OVER!")
                        elif user_choice_3.lower() == "interpret the prophecy your own way":
                            print("Your interpretation leads you to the artifact. The Atlanteans are grateful and grant you the power to control storms. Congratulations!")
                            sys.exit("You have completed your adventure. GAME OVER!")
                        else:
                            print("You've chosen the wrong path! Try again.")
                            print()
                elif user_choice_2.lower() == "search for a map of the city":
                    while True:
                        print("You find a map but it’s incomplete. Will you:")
                        print("* SEARCH FOR THE MISSING PIECES")
                        print("* ASK AN ATLANTEAN SCHOLAR TO HELP FILL IN THE GAPS")
                        print("* TRY TO DECIPHER THE MAP WITH WHAT YOU HAVE")

                        user_choice_3 = str(input("What will you do next? "))
                        print()

                        if user_choice_3.lower() == "search for the missing pieces":
                            print("You find the missing pieces and locate the artifact. The Atlanteans are grateful and grant you the power to control ice. Congratulations!")
                            sys.exit("You have completed your adventure. GAME OVER!")
                        elif user_choice_3.lower() == "ask an atlantean scholar to help fill in the gaps":
                            print("The scholar helps you complete the map and you find the artifact. The Atlanteans are grateful and grant you the power to control the weather. Congratulations!")
                            sys.exit("You have completed your adventure. GAME OVER!")
                        elif user_choice_3.lower() == "try to decipher the map with what you have":
                            print("You decipher the map and find the artifact. The Atlanteans are grateful and grant you the power to control the seas. Congratulations!")
                            sys.exit("You have completed your adventure. GAME OVER!")
                        else:
                            print("You've chosen the wrong path! Try again.")
                            print()
                else:
                    print("You've chosen the wrong path! Try again.")
                    print()      
        else:
            print("You've chosen the wrong book! Try again.")
            print()
