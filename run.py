import random
import sys
import time
import simple_colors

'''
SAVE THE VISION is a Genshin Impact adventure made in hangman style game. 
Created by Jordana Braga using Python. 
'''

# Function to display text as if typed

def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(6./90)

'''
In Genshin Impact, characters gain elemental powers when they receive an object called a Vision. 

The section below define variables using the import random to be able to radomly assign a type of vision to the player. 
'''

# Variable for the List of elements
elements = ['pyro', 'hydro', 'dendro', 'anemo', 'electro', 'geo', 'cryo']

# Variable that selects a random element from the elements list
random_element = random.choice(elements)


'''
The section below defines functions including lists that are referenced in the game. 
First, the random name of the character that will be guessed by the player.
And second, the ASCII drawing that represents the enemy getting closer
to steal the Vision from the player. 
'''

# Function that includes a list of Genshin characters names and then it
# returns a random name from the list

def random_characters():
    genshin_characters = [
        'Diluc', 'Jean', 'Mona', 'Keqing', 'Venti', 'Klee', 'Qiqi', 'Ganyu',
        'Xiao', 'Albedo', 'Eula', 'Zhongli', 'Childe', 'Hu Tao', 'Ayaka',
        'Rosaria', 'Beidou', 'Xingqiu', 'Sucrose', 'Ningguang', 'Xiangling',
        'Barbara', 'Fischl', 'Kaeya', 'Lisa', 'Amber', 'Noelle', 'Razor',
        'Bennett', 'Chongyun', 'Diona', 'Xinyan', 'Sayu', 'Yanfei', 'Cyno', 
        'Tighnari', 'Collei', 'Dori', 'Alhaitham', 'Dehya', 'Nilou', 'Nahida', 
        'Candace', 'Kaveh', 'Layla', 'Faruzan', 'Itto', 'Gorou', 'Kazuha', 
        'Ayaka', 'Ayato', 'Kirara', 'Sara', 'Kuki', 'Shogun', 'Kokomi', 'Heizou', 
        'Thoma', 'Yae', 'Yoimiya', 'Charlotte', 'Freminet', 'Furina', 'Lynette', 
        'Lyney', 'Neuvillette', 'Wriothesley', 'Navia', 'Clorinde', 'Sigewinne', 
        'Arlecchino', 'Baizhu', 'Dainsleif'
    ]
    return random.choice(genshin_characters).upper()


# Function with the ASCII drawing that is returned in stages

def display_hangman(tries):
    stages = [
        r'''
             ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ｡⋆ ☁︎｡⋆｡ ﾟ⋆       
                                           +
                                         O/   
       ---------------------------------/|  
                                        / \    
    ========================================
        ''',
        r'''
              ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ｡⋆ ☁︎｡⋆｡ ﾟ⋆        
         
                                   O   
       ---------------------------/|\-- +  
                                  / \    
    ========================================
        ''',
       r'''
             ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ｡⋆ ☁︎｡⋆｡ ﾟ⋆
         
                             O   
       ---------------------/|\-------- +  
                            / \    
    ========================================
        ''',
        r'''
             ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ｡⋆ ☁︎｡⋆｡ ﾟ⋆         
         
                       O   
       ---------------/|\-------------- +  
                      / \    
    ========================================
        ''',
        r'''
             ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ｡⋆ ☁︎｡⋆｡ ﾟ⋆        
         
                 O   
       ---------/|\-------------------- +  
                / \    
    ========================================
        ''',
        r'''
             ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ｡⋆ ☁︎｡⋆｡ ﾟ⋆        
         
           O   
       ---/|\-------------------------- +  
          / \    
    ========================================
        ''',
        r'''
             ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ﾟ｡⋆ ☁︎｡⋆｡ ﾟ⋆        
         
        O   
       /|\----------------------------- +  
       / \    
    ========================================
        '''
    ]

    return stages[tries]


'''
This function defines the mechanics of the game.
In this game the player type letters or words trying to match a secret word.
The function provides feedback to say if the input is right, wrong or not valid.
It also had a hint system. 
And it counts the number of tries to see if the player will lose or win.

This is accomplished by defining variables first, then providing an input
with a while loop that includes a series of if else statements covering 
possible answer scenarios, and printing the feedback.
'''

def game(genshin_characters):
    word_completion = "_" * len(genshin_characters)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    hint = "paimon"
    print(f"\nLet's play, {name.capitalize()}!")
    print(simple_colors.cyan(display_hangman(tries)))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input(simple_colors.green("Who is coming to help you? \n")).upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\nYou've already guessed", guess)
            elif guess not in genshin_characters:
                print("\n", guess, "is not in the name.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("\nGood job,", guess, "is in the name!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(genshin_characters) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(genshin_characters) and guess.isalpha():
            if guess in guessed_words:
                print("\nYou've already guessed", guess)
            elif guess != genshin_characters:
                print("\n", guess, "is not in the name.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = genshin_characters
        
        elif len(guess) == len(hint):
            print(simple_colors.yellow(f"\n>->->->-> Hi, {name.capitalize()}! ・゜ʚɞ ゜゜\n>->->->-> Maybe we should try the letter {random.choice(genshin_characters)}."))

        else:
            print("\nNot a valid guess.")

        print("\n<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>")
        print(simple_colors.cyan(display_hangman(tries)))
        print(word_completion)
        print("\nGuessed letters:", guessed_letters)
        print("\n˚₊‧꒰ა  ʚ If you need help, type 'paimon' to receive a hint. ɞ  ໒꒱ ‧₊˚")
        print("\n")

    if guessed:
        sprint(simple_colors.yellow(f"You got it, {name.capitalize()}! {genshin_characters.title()} is here to help you!\nTogether you form the best adventuring due and\n no Fatui agent can steal your {random_element.capitalize()} vision from you.\n"))
    else:
        sprint(simple_colors.yellow(f"Oh no, the Fatui agent stole your vision! You didn't discover {genshin_characters.title()} in time.\n"))


'''
Series of terminal prints to introduce the game.
'''

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

name = input("\nHello, Traveler! What is your name?\n")

sprint(f"\n{name.capitalize()}, the gods have blessed you with the {random_element.capitalize()} vision. \n")

sprint('Oh no! Now a Fatui agent is trying to steal it!\n')

sprint('Can you guess who is coming to help you?\n')

sprint(simple_colors.green("Instructions: This is a Hangman style game.\nGuess the letters from a Genshin Impact character's name.\nIncorrect guesses bring the Fatui agent closer to the Vision. \n"))


'''
The main function using the game function and creating a 
while loop to allows players to restart the game
'''

def main():
    genshin_characters = random_characters()
    game(genshin_characters)
    while input("Want to go adventuring again? (Y/N): ").upper() == "Y":
        genshin_characters = random_characters()
        game(genshin_characters)

if __name__ == "__main__":
    main()
