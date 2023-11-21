import random, sys, time
import simple_colors







# Main function
def main():
    genshin_characters = random_characters()
    game(genshin_characters)
    while input("Want to go adventuring again? (Y/N): ").upper() == "Y":
        genshin_characters = random_characters()
        game(genshin_characters)

if __name__ == "__main__":
    main()
