### Playable in a terminal ###
import random
possible_words = [
    "computer", "programming", "hangman", "developer", "language", "software",
    "algorithm", "keyboard", "function", "variable", "debugging", "recursion",
    "condition", "iteration", "framework", "application", "repository",
    "database", "networking", "encryption", "excellent", "challenge", "victory",
    "knowledge", "solution", "creative", "passion", "success", "education",
    "experience", "efficiency", "communication", "dedication", "flexibility",
    "independence", "motivation", "responsibility", "collaboration",
    "innovation", "imagination", "leadership", "organization", "productivity",
    "technology", "effort", "inspiration", "enthusiasm", "perseverance"
]

random_word = random.choice(possible_words).upper()
points = 0
print(f"\033[8m{random_word}\033[0m")
full_guess = []
guess_word = []
[guess_word.append("_") for i in range(len(random_word))]

while True:
    if points >= 11: ## You lose the game because of points
            print("\033[41mEnd of the game, you are hanged!\033[0m")
            print(f"{random_word.capitalize()}: was the word..")
            exit() ### End of the Game
    if "_" not in guess_word: ## You win the game because of no more letter to found
            print(f"{random_word.capitalize()}: correct guess")
            print("\033[42mCongratulations !\033[0m")
            if points <= 1:
                 print(f"{points} point")
            else :   
                print(f"{points} points")
            exit() ### End of the Game
    [print(o,end = " ") for o in guess_word] # Print the partial word with "_" or letter
    if points <= 1: # Add the total points at the end
        print(f" / {points} point")
    else :   
        print(f" / {points} points")
    print("")

    guess = str(input("> ")).upper()
    full_guess.append(guess)
    match_guess = 0
    if len(guess) == 1: # Guess a letter
        for letter_match_pos in range(len(random_word)): # Watch if there is the guess letter in the word 
            if random_word[letter_match_pos] == guess: 
                guess_word[letter_match_pos] = guess # Replace the "_" with the correct letter found
                match_guess += 1
        if match_guess >=1: # Match for the word
            print(f"\033[0;32mFound {match_guess} {guess}\033[0m")
        else: # Does not match for the word
            print(f"\033[0;33mNo {guess} found\033[0m")
            points += 1

    elif len(guess) >= 2: # Guess a word (more than one letter)
        if guess != random_word: # Did not found the correct word
            print(f"{guess}: incorrect guess")
            points += 1
        elif guess == random_word: ## You win the game because of word found
            print(f"{guess}: correct guess")
            print("\033[42mCongratulations !\033[0m")
            if points <= 1:
                 print(f"{points} point")
            else :   
                print(f"{points} points")
            exit() ### End of the Game

    [print(f"\033[3m{g}\033[0m",end = " ") for g in full_guess] # Show all the guess you made
    print("")


'''### Playable in a tkinter ###
import tkinter
from tkinter import *
import customtkinter
import random
import threading
import time

possible_words = [
    "computer", "programming", "hangman", "developer", "language", "software",
    "algorithm", "keyboard", "function", "variable", "debugging", "recursion",
    "condition", "iteration", "framework", "application", "repository",
    "database", "networking", "encryption", "excellent", "challenge", "victory",
    "knowledge", "solution", "creative", "passion", "success", "education",
    "experience", "efficiency", "communication", "dedication", "flexibility",
    "independence", "motivation", "responsibility", "collaboration",
    "innovation", "imagination", "leadership", "organization", "productivity",
    "technology", "effort", "inspiration", "enthusiasm", "perseverance"
]'''

'''game_infos = ""

def start_gui():
    global game_infos
    app = customtkinter.CTk()
    picturebox = customtkinter.CTkLabel(app, width=200, height=200, text="")
    textbox = customtkinter.CTkLabel(app, width=200, height=100, text="Welcome to Hangman Game\nThe objective is to guess a word\n\nEnter a letter or word")
    guessbox = customtkinter.CTkLabel(app, width=200, height=50, text="")
    textbox.pack()
    guessbox.pack()
    picturebox.pack()

    inputbox = customtkinter.CTkEntry(app)
    inputbox.pack()

    inputbox.configure(state="normal")

    def submit():
        global guess_input
        global game_infos
        global guess_box
        guess_input = inputbox.get().upper()
        textbox.configure(text=game_infos)
        guessbox.configure(text=guess_box)
        app.update_idletasks()



    button = customtkinter.CTkButton(master=app, text="Submit", command=submit)
    button.pack()

    # Start the game logic in a separate thread
    game_thread = threading.Thread(target=run_game)
    game_thread.start()

    app.mainloop()

def run_game():
    global game_infos
    global guess_box
    global guess_input
    guess = ""
    guess_input = ""
    guess_box = ""
    random_word = random.choice(possible_words).upper()
    points = 0
    print(f"\033[8m{random_word}\033[0m")
    full_guess = []
    guess_word = []
    [guess_word.append("_") for i in range(len(random_word))]
    while True:
        game_infos = ""
        if points >= 11: ## You lose the game because of points
                print("\033[41mEnd of the game, you are hanged!\033[0m")
                print(f"{random_word.capitalize()}: was the word..")
                exit() ### End of the Game
        if "_" not in guess_word: ## You win the game because of no more letter to found
                print(f"{random_word.capitalize()}: correct guess")
                print("\033[42mCongratulations !\033[0m")
                if points <= 1:
                    print(f"{points} point")
                else :   
                    print(f"{points} points")
                exit() ### End of the Game
        game_infos = ""
        game_infos = " ".join(o for o in guess_word)
        if points <= 1: # Add the total points at the end
            print(f" / {points} point")
        else :   
            print(f" / {points} points")
        print("")

        past_guess = guess ## Wait for interface input
        while guess == past_guess: 
            time.sleep(1)
            guess = guess_input
        full_guess.append(guess)
        match_guess = 0
        if len(guess) == 1: # Guess a letter
            for letter_match_pos in range(len(random_word)): # Watch if there is the guess letter in the word 
                if random_word[letter_match_pos] == guess: 
                    guess_word[letter_match_pos] = guess # Replace the "_" with the correct letter found
                    match_guess += 1
            if match_guess >=1: # Match for the word
                print(f"\033[0;32mFound {match_guess} {guess}\033[0m")
            else: # Does not match for the word
                print(f"\033[0;33mNo {guess} found\033[0m")
                points += 1

        elif len(guess) >= 2: # Guess a word (more than one letter)
            if guess != random_word: # Did not found the correct word
                print(f"{guess}: incorrect guess")
                points += 1
            elif guess == random_word: ## You win the game because of word found
                print(f"{guess}: correct guess")
                print("\033[42mCongratulations !\033[0m")
                if points <= 1:
                    print(f"{points} point")
                else :   
                    print(f"{points} points")
                exit() ### End of the Game

        guess_box = " ".join(g for g in full_guess)
        [print(f"\033[3m{g}\033[0m",end = " ") for g in full_guess] # Show all the guess you made
        print("")

start_gui()'''