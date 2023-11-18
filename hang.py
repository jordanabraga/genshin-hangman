import random, sys, time
import simple_colors

def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(6./90)


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

# List of elements
elements = ['pyro', 'hydro', 'dendro', 'anemo', 'electro', 'geo', 'cryo']

# Randomly select one element from the list
random_element = random.choice(elements)

sprint(f"\n{name.capitalize()}, the gods have blessed you with the {random_element.capitalize()} vision. \n")

sprint('But now a Fatui agent is trying to steal it!\n')

sprint('Can you guess who is coming to help you?\n')

sprint(simple_colors.green("Instructions: This is a Hangman style game. Guess the letters from a Genshin Impact character's name.\nIncorrect guesses bring the Fatui agent closer to the Vision. \n"))

# Function that selects a random name from the list to be used in the game
def random_characters():
    genshin_characters = [
        'Diluc', 'Jean', 'Mona', 'Keqing', 'Venti', 'Klee', 'Qiqi', 'Ganyu',
        'Xiao', 'Albedo', 'Eula', 'Zhongli', 'Childe', 'Hu Tao', 'Ayaka',
        'Rosaria', 'Beidou', 'Xingqiu', 'Sucrose', 'Ningguang', 'Xiangling',
        'Barbara', 'Fischl', 'Kaeya', 'Lisa', 'Amber', 'Noelle', 'Razor',
        'Bennett', 'Chongyun', 'Diona', 'Xinyan', 'Sayu', 'Yanfei', 'Childe'
    ]
    return random.choice(genshin_characters).upper()

# Function to display the hangman stages
def display_hangman(tries):
    stages = [
        r'''
       
                                           +
                                         O/   
       ---------------------------------/|  
                                        / \    
    ========================================
        ''',
        r'''
         
         
                                   O   
       ---------------------------/|\-- +  
                                  / \    
    ========================================
        ''',
       r'''
         
         
                             O   
       ---------------------/|\-------- +  
                            / \    
    ========================================
        ''',
        r'''
         
         
                       O   
       ---------------/|\-------------- +  
                      / \    
    ========================================
        ''',
        r'''
        
         
                 O   
       ---------/|\-------------------- +  
                / \    
    ========================================
        ''',
        r'''
        
         
           O   
       ---/|\-------------------------- +  
          / \    
    ========================================
        ''',
        r'''
        
         
        O   
       /|\----------------------------- +  
       / \    
    ========================================
        '''
    ]

    return stages[tries]

# Game function
def game(genshin_characters):
    word_completion = "_" * len(genshin_characters)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(f"\nLet's play, {name.capitalize()}!")
    print(simple_colors.cyan(display_hangman(tries)))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input(simple_colors.green("Who is coming to help you? \n")).upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\n You've already guessed", guess)
            elif guess not in genshin_characters:
                print("\n", guess, "is not in the name.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("\n Good job,", guess, "is in the name!")
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
                print("\n You've already guessed", guess)
            elif guess != genshin_characters:
                print("\n", guess, "is not in the name.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = genshin_characters
        else:
            print("\nNot a valid guess.")

        print(simple_colors.cyan(display_hangman(tries)))
        print(word_completion)
        print("\nGuessed letters:", guessed_letters)
        print("\n")

    if guessed:
        sprint(simple_colors.yellow(f"You got it, {name.capitalize()}! {genshin_characters.title()} is here to help you!\nTogether you form the best adventuring due and no Fatui agent can steal your {random_element.capitalize()} vision from you.\n"))
    else:
        sprint(simple_colors.yellow(f"Oh no, the Fatui agent stole your vision! You didn't discover {genshin_characters.title()} in time.\n"))

# Main function
def main():
    genshin_characters = random_characters()
    game(genshin_characters)
    while input("Want to go adventuring again? (Y/N): ").upper() == "Y":
        genshin_characters = random_characters()
        game(genshin_characters)

if __name__ == "__main__":
    main()
