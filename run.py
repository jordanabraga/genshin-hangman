import random
import sys
import time
import simple_colors

'''
SAVE THE VISION is a Genshin Impact adventure made in hangman style game. 
Created by Dana Braga using Python. 
'''

# Function to display text as if typed

def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(6./90)

'''
In Genshin Impact, characters gain elemental powers when they receive an object called a Vision. 

This part of the code define variables using the import random to be able to radomly assign a type of vision to the player. 
'''

# Variable for the List of elements
elements = ['pyro', 'hydro', 'dendro', 'anemo', 'electro', 'geo', 'cryo']

# Variable that selects a random element from the elements list
random_element = random.choice(elements)