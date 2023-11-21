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