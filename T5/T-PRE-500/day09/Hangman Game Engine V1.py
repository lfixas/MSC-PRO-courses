import customtkinter
import random
import string
import csv
import os
import requests

def get_words(count=200):
    url = f"https://random-word-api.herokuapp.com/word?number={count}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch common words. Status code: {response.status_code}")
        return

words = get_words()

global current_directory, filename, game_data_file_path
current_directory = os.path.dirname(os.path.abspath(__file__))
filename = "hangman_scores.csv"
game_data_file_path = os.path.join(current_directory, filename)

difficulty_value = 11
timer_value = 0
timer_running = False
picture_box = "     o/\n    /|\n    /\\"

rules_visible = False

def open_rule():
    global rules_visible
    global rules_textbox

    if not rules_visible:
        rules_textbox = customtkinter.CTkTextbox(sidebar_frame)
        rules_textbox.grid(row=3, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        rules_textbox.insert("1.0", """Hangman Game Rules:\n\nObjective:\nThe goal of the game is to guess a hidden word or phrase correctly before running out of attempts.\n\nNumber of Attempts:\nThe players have a limited number of attempts or guesses to reveal the hidden word correctly. Players are allowed ten incorrect guesses before losing the game.\n\nGuessing a Letter:\nPlayers take turns guessing letters that they believe might be in the hidden word. If the guessed letter is in the word, it is revealed in its correct position(s). For example, if "A" is guessed and it appears twice in the word, the word "_ A _ _ A" would be revealed. If the guessed letter is not in the word, a part of a "hangman" figure is drawn (e.g., a head, body, arms, legs).\n\nWord Completion:\nThe game continues until one of the following outcomes:The players successfully guess the entire word or phrase, in which case they win the game. The "hangman" figure is completed (typically with a head, body, two arms, and two legs), indicating that the players have run out of attempts. In this case, they lose the game.\n\nWinning:\nPlayers win by guessing the word or phrase correctly within the allowed number of attempts.\n\nLosing:\nPlayers lose if they use up all their allowed guesses without correctly guessing the word or phrase. \n\n\nRemember, Hangman is a classic word-guessing game that can be played in various ways and adapted to suit different preferences and age groups. Have fun playing!""")
        rules_visible = True
    else:
        rules_textbox.grid_forget()
        rules_visible = False

scores_visible = False

def open_scores():
    global scores_visible
    global scores_textbox

    if not scores_visible:
        scores_textbox = customtkinter.CTkTextbox(sidebar_frame)
        scores_textbox.grid(row=4, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        scores_text = "Top 10 Best Scores:\n\n"
        scores_visible = True
        with open(game_data_file_path, mode="r") as file:
            reader = csv.reader(file)
            sorted_scores = sorted(reader, key=lambda x: float(x[1]))[:10]
            for i, row in enumerate(sorted_scores, start=1):
                word, time_taken, lives_used = row
                scores_text += f"------------------ {i} ------------------\n • Word: {word}\n • Time Taken: {time_taken} seconds\n • Lives Used: {lives_used}\n"
        
        scores_textbox.insert("1.0", scores_text)
    else:
        scores_textbox.grid_forget()
        scores_visible = False

def update_timer():
    global timer_value
    timer.configure(text=f"Timer: {timer_value} seconds")
    if timer_running:
        timer_value += 1
        timer.after(1000, update_timer)

def start_timer():
    global timer_running, timer_value
    timer_value = 0
    if not timer_running:
        timer_running = True
        update_timer()

def pictures(points):
    global picture_box
    global difficulty_value
    hang_state = int((11/difficulty_value)*points)
    if hang_state == 1:
        picture_box = "\n\n\n\n\n\n ____    "
    if hang_state == 2:
        picture_box = "\n   |      \n   |      \n   |      \n   |      \n   |      \n __|__    "
    if hang_state == 3:
        picture_box = "   _____ \n   |      \n   |      \n   |      \n   |      \n   |      \n __|__    "
    if hang_state == 4:
        picture_box = "   _____ \n   |/     \n   |      \n   |      \n   |      \n   |      \n __|__    "
    if hang_state == 5:
        picture_box = "   _____ \n   |/  |  \n   |      \n   |      \n   |      \n   |      \n __|__    "
    if hang_state == 6:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |      \n   |      \n   |      \n __|__    "
    if hang_state == 7:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |   | \n   |      \n   |      \n __|__    "
    if hang_state == 8:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |   |\\\n   |      \n   |      \n __|__    "
    if hang_state == 9:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |  /|\\\n   |      \n   |      \n __|__    "
    if hang_state == 10:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |  /|\\\n   |    \\\n   |      \n __|__    "
    if hang_state >= 11:
        picture_box = "   _____ \n   |/  |  \n   |   o \n   |  /|\\\n   |   /\\\n   |      \n __|__    "

def save_game_data(word, time_taken, points):
    with open(game_data_file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([word, time_taken, points])

def new_game():
    global guess_box, guess_input, picture_box, info_result, guess, past_guess, match_guess, points, guess_word, difficulty_value, full_guess, random_word, resultbox, timer_running
    guess = ""
    guess_input = ""
    info_result = ""
    random_word = random.choice(words).upper()
    points = 0
    print(f"\033[8m{random_word}\033[0m")
    full_guess = []
    guess_word = ["_" for _ in range(len(random_word))]
    set_letter_buttons_state("normal")
    textbox.configure(text="Welcome to Hangman Game\nThe objective is to guess a word")
    # guessbox.configure(text="") # If you want to add an history 1/4
    resultbox.grid_forget()
    resultbox = customtkinter.CTkLabel(game_frame, width=200, height=50, text="")
    resultbox.grid(row=1, column=1, rowspan=4, sticky="nsew")
    picture_box = "     o/\n    /|\n    /\\"
    start_game()
    start_timer()
    refresh()

def set_letter_buttons_state(state):
    for button in letter_buttons:
        button.configure(state=state)

def submit():
    global guess_input
    global guess_box
    guess_input = inputbox.get().upper()
    if len(guess_input) >1:
        player_input()
        refresh()

def button_click(letter, button):
    global guess_input
    if not timer_running:
        start_timer()
    guess_input = letter
    player_input()
    refresh()
    button.configure(state="disabled")


def refresh():
    textbox.configure(text=game_infos, font=customtkinter.CTkFont(size=16, weight="bold"))
    # guessbox.configure(text=guess_box) # If you want to add an history 2/4
    picturebox.configure(text=picture_box, font=customtkinter.CTkFont(size=16, weight="bold"))
    if info_result == "Win":
        resultbox.configure(text="Congratulations !", fg_color="lime", text_color="yellow", font=customtkinter.CTkFont(size=16, weight="bold"))
    if info_result == "Lose":
        resultbox.configure(text="End of the game,\nyou are hanged!", fg_color="red", text_color="yellow", font=customtkinter.CTkFont(size=16, weight="bold"))
    if info_result == "Found":
        resultbox.configure(text=f"Found {match_guess} {guess}", text_color="blue", font=customtkinter.CTkFont(size=16, weight="bold"))
    if info_result == "No_Found":
        resultbox.configure(text=f"No {guess} found", text_color="yellow", font=customtkinter.CTkFont(size=16, weight="bold"))
    if info_result == "Wrong_Word":
        resultbox.configure(text=f"{guess.upper()}: incorrect guess", text_color="yellow", font=customtkinter.CTkFont(size=16, weight="bold"))
    if info_result == "Correct_Word":
        resultbox.configure(text=f"{guess.upper()}: correct guess", text_color="lime", font=customtkinter.CTkFont(size=16, weight="bold"))
    
guess = ""
past_guess = ""
guess_input = ""
info_result = ""
random_word = random.choice(words).upper()
points = 0
print(f"\033[8m{random_word}\033[0m")
full_guess = []
guess_word = ["_" for _ in range(len(random_word))]

def difficulty(value):
    global difficulty_value
    difficulty_value = int(value)

def start_game():
    global game_infos
   
    game_infos = " ".join(guess_word)

def player_input():
    global game_infos
    global guess_box
    global guess_input
    global picture_box
    global info_result
    global guess
    global past_guess
    global match_guess
    global points
    global guess_word
    guess = guess_input
    global difficulty_value
    global timer_running

    if guess != past_guess:
        past_guess = guess
        full_guess.append(guess)
        match_guess = 0
        
        if len(guess) == 1:
            for i, letter in enumerate(random_word):
                if letter == guess:
                    guess_word[i] = guess
                    game_infos = guess_word
                    match_guess += 1
            if match_guess >= 1:
                info_result = "Found"
            else:
                info_result = "No_Found"
                points += 1
        
        elif len(guess) >= 2:
            if guess != random_word:
                info_result = "Wrong_Word"
                points += 1
            elif guess == random_word:
                game_infos = guess
                info_result = "Win"
                timer_running = False             
                save_game_data(random_word, timer_value, points)
                # exit()
        
        guess_box = " ".join(full_guess)
        refresh()
        pictures(points)
        if points >= difficulty_value:
            info_result = "Lose"
            game_infos = f"{random_word.upper()} was the word.."
            timer_running = False
            # exit()
        
        if "_" not in guess_word:
            game_infos = f"{random_word.upper()}"
            info_result = "Win"
            timer_running = False
            save_game_data(random_word, timer_value, points)
            # exit()

app = customtkinter.CTk()
app.title("Hangman Game Engine")

app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((0, 2), weight=0)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

sidebar_frame = customtkinter.CTkFrame(app, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=200, sticky="nsw")
sidebar_frame.grid_rowconfigure(4, weight=1)
logo_label = customtkinter.CTkLabel(sidebar_frame, text="Hangman Game", font=customtkinter.CTkFont(size=20, weight="bold")) ###
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
sidebar_new_game = customtkinter.CTkButton(sidebar_frame, text="New Game", command=new_game)
sidebar_new_game.grid(row=1, column=0, padx=20, pady=10)
rules_button = customtkinter.CTkButton(sidebar_frame, text="Rules", command=open_rule)
rules_button.grid(row=2, column=0, padx=20, pady=(10, 10))
scores_button = customtkinter.CTkButton(sidebar_frame, text="Best Scores", command=open_scores)
scores_button.grid(row=3, column=0, padx=20, pady=(10, 10))
lives_label = customtkinter.CTkLabel(sidebar_frame, text="Lifes", anchor="w")
lives_label.grid(row=8, column=0, padx=20, pady=(10, 0))
difficulty_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"], command=difficulty)
difficulty_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))
autor_label = customtkinter.CTkLabel(sidebar_frame, text="By Lucas Fixari", anchor="sw", font=customtkinter.CTkFont(size=8))
autor_label.grid(row=50, column=0, padx=20, pady=(5, 0))

### key sidebar ###
key_sidebar_frame = customtkinter.CTkFrame(app, width=140, corner_radius=4)
key_sidebar_frame.grid(row=0, column=2, rowspan=99, sticky="nse", padx=5, pady=5)

button_width = 28  # Adjust key button
button_height = button_width

# Generate alphabet buttons in rows of 4
buttons_per_row = 4
button_count = 0

## key alphabet
letter_buttons = []
for letter in string.ascii_uppercase:
    button = customtkinter.CTkButton(key_sidebar_frame, text=letter, font=customtkinter.CTkFont(size=15, weight="bold"), width=button_width, height=button_height)
    button.grid(row=button_count//buttons_per_row+1, column=button_count%buttons_per_row, padx=3, pady=3)
    button_count += 1
    button.configure(command=lambda b=button, l=letter: button_click(l, b))
    letter_buttons.append(button)

### game_frame
game_frame = customtkinter.CTkFrame(app, fg_color="transparent")
game_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
game_frame.grid_rowconfigure(4, weight=1)

textbox = customtkinter.CTkLabel(game_frame, width=200, height=50, text="Welcome to Hangman Game\nThe objective is to guess a word")
# guessbox = customtkinter.CTkLabel(game_frame, width=200, height=50, text="") # If you want to add an history 3/4
resultbox = customtkinter.CTkLabel(game_frame, width=200, height=50, text="")
picturebox = customtkinter.CTkLabel(game_frame, width=200, height=200, bg_color="#1E1E1E", text="", font=customtkinter.CTkFont(size=20, weight="bold"), corner_radius=4)

textbox.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)
resultbox.grid(row=1, column=1, rowspan=4, sticky="nsew")
# guessbox.grid(row=5, column=1, rowspan=4, sticky="nsew") # If you want to add an history 4/4
picturebox.grid(column=1, rowspan=4, sticky="s")

inputbox = customtkinter.CTkEntry(app, placeholder_text="Guess the word")
inputbox.grid(row=100, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
inputbox.configure(state="normal")

button_submit = customtkinter.CTkButton(app, text="Submit", command=submit)
button_submit.grid(row=100, column=2, columnspan=2, padx=(5, 5), pady=(20, 20), sticky="nsew")

# timer
timer_frame = customtkinter.CTkFrame(key_sidebar_frame, corner_radius=0)
timer_frame.grid(row=0, column=0, sticky="n", columnspan=4, padx=5, pady=5)
timer = customtkinter.CTkLabel(timer_frame, text=f"Timer: {timer_value} seconds", font=customtkinter.CTkFont(size=12), width=130)
timer.grid(row=0, column=0, padx=20, pady=20)

update_timer()

### Add bgm in game ###
# import pygame
# pygame.mixer.init()
# def play():
#     current_directory = os.path.dirname(os.path.abspath(__file__))
#     bgm = "bgm.mp3"
#     bgm_file_path = os.path.join(current_directory, bgm)
#     pygame.mixer.music.load(bgm_file_path)
#     pygame.mixer.music.play(loops=1)
# play()
#####

start_game()
app.mainloop()