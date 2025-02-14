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
]

game_infos = ""
picture_box = "     o/\n    /|\n    /\\"

def pictures(points):
    global picture_box
    if points == 1:
        picture_box = "\n\n\n\n\n\n ____    "
    if points == 2:
        picture_box = "\n   |      \n   |      \n   |      \n   |      \n   |      \n __|__    "
    if points == 3:
        picture_box = "   _____ \n   |      \n   |      \n   |      \n   |      \n   |      \n __|__    "
    if points == 4:
        picture_box = "   _____ \n   |/     \n   |      \n   |      \n   |      \n   |      \n __|__    "
    if points == 5:
        picture_box = "   _____ \n   |/  |  \n   |      \n   |      \n   |      \n   |      \n __|__    "
    if points == 6:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |      \n   |      \n   |      \n __|__    "
    if points == 7:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |   | \n   |      \n   |      \n __|__    "
    if points == 8:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |   |\\\n   |      \n   |      \n __|__    "
    if points == 9:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |  /|\\\n   |      \n   |      \n __|__    "
    if points == 10:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |  /|\\\n   |    \\\n   |      \n __|__    "
    if points >= 11:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |  /|\\\n   |   /\\\n   |      \n __|__    "

def submit():
    global guess_input
    global game_infos
    global guess_box
    guess_input = inputbox.get().upper()
    refresh()

def refresh():
    textbox.configure(text=game_infos)
    guessbox.configure(text=guess_box)
    picturebox.configure(text=picture_box)
    if info_result == "Win":
        resultbox.configure(text="Congratulations !", fg_color="lime", font=("Arial", 16, "bold"))
    if info_result == "Lose":
        resultbox.configure(text="End of the game, you are hanged!", fg_color="red", font=("Arial", 16, "bold"))
    if info_result == "Found":
        resultbox.configure(text=f"Found {match_guess} {guess}", text_color="blue", font=("Arial", 16, "bold"))
    if info_result == "No_Found":
        resultbox.configure(text=f"No {guess} found", text_color="yellow", font=("Arial", 16, "bold"))
    

def run_game():
    global game_infos
    global guess_box
    global guess_input
    global picture_box
    global info_result
    global guess
    global match_guess
    guess = ""
    guess_input = ""
    guess_box = ""
    info_result = ""
    random_word = random.choice(possible_words).upper()
    points = 0
    print(f"\033[8m{random_word}\033[0m")
    full_guess = []
    guess_word = ["_" for _ in range(len(random_word))]
    
    while True:
        game_infos = ""
        if points >= 11:
            info_result = "Lose"
            game_infos = f"{random_word.capitalize()}: was the word.."
            exit()
        
        if "_" not in guess_word:
            game_infos = f"{random_word.capitalize()}: correct guess"
            info_result = "Win"
            exit()
        
        game_infos = " ".join(guess_word)
        
        refresh()
        past_guess = guess
        while guess == past_guess:
            time.sleep(1)
            guess = guess_input
        
        full_guess.append(guess)
        match_guess = 0
        
        if len(guess) == 1:
            for i, letter in enumerate(random_word):
                if letter == guess:
                    guess_word[i] = guess
                    match_guess += 1
            if match_guess >= 1:
                info_result = "Found"
            else:
                info_result = "No_Found"
                points += 1
        
        elif len(guess) >= 2:
            if guess != random_word:
                game_infost = f"{guess}: incorrect guess"
                points += 1
            elif guess == random_word:
                game_infos = f"{guess}: correct guess"
                info_result = "Win"
                exit()
        
        guess_box = " ".join(full_guess)
        pictures(points)

app = customtkinter.CTk()
app.title("Hangman Game Engine")
textbox = customtkinter.CTkLabel(app, width=200, height=100, text="Welcome to Hangman Game\nThe objective is to guess a word\n\nEnter a letter or word")
guessbox = customtkinter.CTkLabel(app, width=200, height=50, text="")
resultbox = customtkinter.CTkLabel(app, width=200, height=50, text="")
picturebox = customtkinter.CTkLabel(app, width=200, height=200, text="", font=customtkinter.CTkFont(size=20, weight="bold"))

textbox.pack()
resultbox.pack()
guessbox.pack()
picturebox.pack()

inputbox = customtkinter.CTkEntry(app)
inputbox.pack()
inputbox.configure(state="normal")

button = customtkinter.CTkButton(master=app, text="Submit", command=submit)
button.pack()

game_thread = threading.Thread(target=run_game)
game_thread.start()

app.mainloop()