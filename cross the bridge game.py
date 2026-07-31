# Cross the bridge to claim your forgotten treasure
print("Welcome to the mini game", ("\U0001F995"))

name = input("What is your name? ")
age = int(input("What is your age? "))

health = 100

if age >= 15:
    while True: # Loop yahan se shuru hoga, naam ke NICHE
        print("ACCESS GRANTED", "\U0001F600", "Ready to Play? \nSooo...")
        player = input("Do you really wanna see what`s hiding in it? ").lower()
        
        if player == "yes":
            print("Ok! You`re starting with ",health, "health!❤️ ")
            print("let`s gooo!")

            left_or_right = input("choose the path, left or right? ")
            if left_or_right == "left":
                ans = input("good way....You are near the lake. 🏞 \n Do you know how to swim? ")

                # --- if swim is yes ---
                if ans == "yes":  
                    swim_choice = input("Great! Wanna swim across, around, or need help? ")

                    #ACROSS -- Waves & Mud Swamp
                    if swim_choice == "across":
                        print("This path is correct, but it`s long and exhausting...\n " "Wait, Huge waves are coming...🌊")

                        wave_action = input("Do you fight the waves or dive under? (fight/dive): ").lower()
                        if wave_action == "dive":
                            health -= 20 # Smooth dive takes less energy
                            print("Smart! You dived under the surface waves smoothly, but Lost 30 health!💔")
                        else:
                            health -= 50 # Fighting heavy waves takes 50 health
                            print("Ouff! Fighting the surface waves exhausted you. \n  You`re tired.😫")
                            print("Fighting cause you lose health! 😓 keep swiming.. ")

                        print(f" Remaining Health: {health}/100")

                        # Mud Swamp at corner of lake
                        print("Now you swim across & reach the opposite shore but suddenly you step into hidden mud swamp!")
                        mud_choice = input("Quick! Do you try to jump or crawl? ")
                        if mud_choice == "crawl":
                            print("Smart move! Crawling saved you from sinking.")
                            print("You finally crossed the bridge and claimed the TREASURE! 🏆")
                        elif mud_choice == "jump": #Jump means Game Over
                            health -= 50 # Sinking takes remaining health n energy
                            print("Current Health: 0")
                            print("Oh no! Jumping made you sink deeper into the mud. Game Over! 😢")

                    # --- Around --- Fish & Crocodile
                    elif swim_choice == "around":
                        print("Oppps! 😢 you`re bitten by fish and lose 30 health!💔")
                        health -= 30
                        print(f"Your Current Health: {health}/100")
                        print("Still alive, keep moving fast...")

                        # Crocodile section
                        print("Ohh noo! 😨 A giant Crocodile blocks your path in the deep water!")
                        croc_choice = input("Do you wanna swim quietly or splash water to scare it? (quiet/splash) ")
                        if croc_choice == "quiet":
                            print("WOWW! You slipped past the Crocodile undetected, reached the bridge, and crossed it safely.")
                            print("The TREASURE is yours!🏆")
                        else:
                            health -= 70 # Takes away all remaining health (30 - 70 <= 0)
                            print("Current Health: 0")
                            print("The splash attracted the Crocodile! It attacked you. Game Over! 🐊")

                    #--- help ---
                    elif swim_choice == "help":
                        print("If you know the swimming you can play along & cross the bridge successfully!\n" "otherwise you can take the boat.")
                        print("Play Cleverly!😉")

                # --- No swin and take boat , another way ---
                elif ans == "no":
                    print("To reach the lake, you must pass through the mysterious Island. 🏝")
                    print("You find a boat anchored near a creepy old house. 🏚️")
                    house_choice = input("Do you want to check the house for supplies or take the boat directly? (house/boat) ")
                    
                    if house_choice == "house":
                        print("Oh no! A Witch lives inside! She attacked you and cast a spell. 🔮")
                        print("You lose 50 health! 💔 ")
                        health -= 50 # Witch takes 50 health
                        print(f"Remaining Health = 50")
                        print("You`re still alive! Run.. 🏃")
                        print("You survived and now outside!")

                        # After escaping from witch - other choice.
                        next_ans = input("There`s another path with a river & forest, which would you choose? ")
                        if next_ans == "forest":
                            print("Oppss! Another trap ☹️ ")
                            health -= 50
                            print(f"Remaining Health = {health}")
                            print("You lost!💔")
                        else:
                            print("You jumped into the river, safely swam to the bridge, and got the TREASURE! 🏆")

                    #choosing boat
                    elif house_choice == "boat":
                        print("Smart move! You avoided the house, took the boat, and get safely down the river.")
                        print("You bypass all dangers 😱, reach the main bridge, and cross it.")
                        print("Congratulations! You found the hidden TREASURE! 🏆")

            # if the player choose right.
            else:
                print("Opps! Lost in the dark woods. Wild beasts🐺 howling...")
                print("oh no! They catch you & attacked. You`re dead!☠️")

        # if player say No    
        else:
            print("ha ha! Goodbye!")
            
        # 1. Har dafa game khatam hone par loop ke end par yeh poochega
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            health = 100 # Health wapas full ho jayegi aglay round ke liye
            print("\nRestarting system... 🚀")
        else:
            print("Thanks for playing! Goodbye! 👋")
            break # Yeh loop ko roke ga aur game band kar dega

else:
    print("Booom! not older to play")
