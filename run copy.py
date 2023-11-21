import random, sys, time
import simple_colors



print(simple_colors.cyan(r'''
   _____                                        
  / ____|                     _                  
 | (___   __ ___   _____    _| |_                
  \___ \ / _` \ \ / / _ \  |_   _|               
  ____) | (_| |\ V /  __/    |_|                 
 |_____/ \__,_| \_/ \___|
 ___  _           __ 
 | | | |          \ \    / (_)   (_)            
 | |_| |__   ___   \ \  / / _ ___ _  ___  _ __  
 | __| '_ \ / _ \   \ \/ / | / __| |/ _ \| '_ \ 
 | |_| | | |  __/    \  /  | \__ \ | (_) | | | |
  \__|_| |_|\___|     \/   |_|___/_|\___/|_| |_|
  '''                                      
))

print(simple_colors.green("--A Genshin Impact adventure as a Hangman game--\n"))
# welcoming the user
name = input("\nHello, Traveler! What is your name?\n")

sprint(f"\n{name.capitalize()}, the gods have blessed you with the {random_element.capitalize()} vision. \n")

sprint('Oh no! Now a Fatui agent is trying to steal it!\n')

sprint('Can you guess who is coming to help you?\n')

sprint(simple_colors.green("Instructions: This is a Hangman style game.\n Guess the letters from a Genshin Impact character's name.\nIncorrect guesses bring the Fatui agent closer to the Vision. \n"))





# Main function
def main():
    genshin_characters = random_characters()
    game(genshin_characters)
    while input("Want to go adventuring again? (Y/N): ").upper() == "Y":
        genshin_characters = random_characters()
        game(genshin_characters)

if __name__ == "__main__":
    main()
