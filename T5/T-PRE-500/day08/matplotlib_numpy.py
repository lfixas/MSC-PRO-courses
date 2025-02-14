import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import random
import math
import os

### matplotlib and numpy ###
## Can you explain the following snippet of code? ##
def matplotlib_numpy_task01():
    '''This code sets up a range from 0 to 10
     and generates an array (x_values) containing 100 
     evenly spaced values within that range.'''
    x_min, x_max = 0, 10
    x_values = np.linspace(x_min, x_max, 100)
    print(x_values)

## Display the points (0; 12), (1; 32), (2; 42) and (3; 52) ##
## in a chart similar to this one: ##
def matplotlib_numpy_task02():
    x_values = [0, 1, 2, 3]
    y_values = [12, 32, 42, 52]

    plt.grid(True)

    plt.ylabel('some numbers')

    plt.scatter(x_values, y_values, label='Data Points', color='red', marker='o')

    plt.show()

## Write a function that takes an array of points as argument ##
## and displays the points in a nice and clean chart. ##
def matplotlib_numpy_task03():
    x_values = np.linspace(1, 1000, 100)
    y_values = [random.randrange(50) for i in range(100)]
    y_values.sort()
    x_values_job = [0, 1000]
    y_values_job = [0, 0]

    plt.plot(x_values, y_values, label='Python', color='blue')
    plt.plot(x_values_job, y_values_job, label='Company that respond to me', color='red')

    plt.xlabel('The time I spent on it')
    plt.ylabel('My competences in Python')
    plt.title('A nice and clean chart')

    plt.legend()
    plt.grid()

    plt.show()

## Write a plt_fct function that plots any function ##
## taking x as a parameter. ##
def matplotlib_numpy_task04():
    def plot_fct(func, x_min, x_max, points=100, title="Function Plot"):
        x_values = np.linspace(x_min, x_max, points)
        y_values = [func(x) for x in x_values]

        plt.plot(x_values, y_values, label='Function Plot', color='blue')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()

    def f(x) :
        return x**2 + x*3 + 2

    plot_fct(math.sin, 0, 50, title="Sine Function")
    plot_fct(f, -100, 200, title="Quadratic Function")
    plot_fct(lambda x: x**2, -10, 10, title="Square Function")
    plot_fct(lambda x: 1/x, -100, 100, title="Inverse Function")
#####

### Tkinter ###
## Open a tk window with a LabelFrame and a Frame in it. ##
def tkinter_task01():
    # Create the main application window
    app = tk.Tk() 
    app.title("LabelFrame and Frame Example")

    # Create a LabelFrame
    label_frame = tk.LabelFrame(app, text="LabelFrame")
    label_frame.pack(padx=10, pady=10)

    # Create a Frame inside the LabelFrame
    inner_frame = tk.Frame(label_frame)
    inner_frame.pack(padx=10, pady=10)

    # Add widgets to the inner Frame (e.g., labels, buttons, etc.)
    label = tk.Label(inner_frame, text="This is inside the Frame") 
    label.pack() 

    # Start the Tkinter main loop
    app.mainloop() 

def tkinter_task01_2():
    # Function to convert text to UPPERCASE
    def convert_to_uppercase():
        user_input = entry.get()
        print(user_input.upper())

    # Create the main application window
    app = tk.Tk()
    app.title("LabelFrame, Entry, and Button Example")

    # Create a LabelFrame
    label_frame = tk.LabelFrame(app, text="LabelFrame")
    label_frame.pack(padx=10, pady=10)

    # Create an Entry (input field) inside the LabelFrame
    entry = tk.Entry(label_frame)
    entry.pack(pady=10)

    # Create a button inside the LabelFrame to convert text to UPPERCASE
    button = tk.Button(label_frame, text="Convert to UPPERCASE", command=convert_to_uppercase)
    button.pack()

    # Start the Tkinter main loop
    app.mainloop()

def tkinter_task02():
    from tkinter import PhotoImage

    # Create the main application window
    app = tk.Tk()
    app.title("Canvas with Background Image Example")

    # Create a Frame
    frame = tk.Frame(app)
    frame.pack()

    # # Create a Canvas inside the Frame
    # canvas = tk.Canvas(frame, width=400, height=300)  # Adjust width and height as needed
    # canvas.pack()

    # Load the background image
    script_dir = os.path.dirname(__file__)
    image_path = os.path.join(script_dir, "background.png")
    background_image = PhotoImage(file=image_path)
    image_width = background_image.width()
    image_height = background_image.height()

    # Create a Canvas inside the Frame
    canvas = tk.Canvas(frame, width=image_width, height=image_height)  # Adjust width and height as needed
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    # Start the Tkinter main loop
    app.mainloop()

tkinter_task02()

def tkinter_task03():
    # Create the main application window
    app = tk.Tk()
    app.geometry("300x300")
    app.title("Stickman Figure")

    # Create a Canvas to draw on
    canvas = tk.Canvas(app, width=200, height=300)
    canvas.pack()

    ## Draw usine create_xx with x_start, y_start, x_end_ y_end
    # Draw the head (a circle)
    canvas.create_oval(80, 20, 120, 60, width=2, outline="lime", fill="lime")

    # Draw the body (a line)
    canvas.create_line(100, 60, 100, 160, width=2, fill="green")

    # Draw the left arm (a line)
    canvas.create_line(100, 80, 60, 120, width=2, fill="red")

    # Draw the right arm (a line)
    canvas.create_line(100, 80, 140, 40, width=2, fill="blue") # 40 -> 120

    # Draw the left leg (a line)
    canvas.create_line(100, 160, 60, 240, width=2, fill="purple")

    # Draw the right leg (a line)
    canvas.create_line(100, 160, 140, 240, width=2, fill="orange")

    # Add the text "Hello World" next to the head
    canvas.create_text(160, 20, text="Coucou twa", fill="black", font=("Arial", 12))


    # Start the Tkinter main loop
    app.mainloop()

def tkinter_task04():
    global x_arm, y_arm, dx_arm, dy_arm, x_text, y_text, dx_text, dy_text, color
    # Create the main application window
    app = tk.Tk()
    app.geometry("300x300")
    app.title("Stickman Figure Animated")

    # Create a Canvas to draw on
    canvas = tk.Canvas(app, width=200, height=300)
    canvas.pack()

    # Initial position of the stickman's right arm
    x_arm, y_arm = 140, 40
    x_text, y_text = 160, 20
    dx_arm, dy_arm = 3, 3 # Speed
    dx_text, dy_text = 2, 0.5

    color = [
    "black", "white", "red", "green", "blue", "cyan", "magenta", "yellow",
    "gray", "pink", "purple", "orange", "brown", "violet", "indigo", "turquoise",
    "dark red", "dark green", "dark blue", "dark gray",
    "light sea green", "maroon", "spring green", "gold", "dim gray",
    "navy blue", "cadet blue", "sienna", "light coral", "medium purple",
    "dark slate gray", "firebrick", "medium aquamarine", "medium blue", "medium orchid",
    "light goldenrod", "medium sea green", "royal blue", "slate gray", "pale violet red",
    "dark olive green", "coral", "medium slate blue", "salmon", "dark salmon",
    "dark violet", "light sky blue", "light salmon", "thistle", "chocolate",
    "dark orange", "medium violet red", "light steel blue", "dark orchid", "pale green",
    "light pink", "sienna", "medium slate blue", "chartreuse", "medium turquoise",
    "medium violet red", "light steel blue", "dark orchid", "pale green", "light pink",
    "peru", "dark orange", "medium violet red", "dark turquoise", "dark khaki",
    "medium spring green", "deep pink", "dodger blue", "medium orchid", "tomato",
    "yellow green", "dark slate blue", "dark goldenrod", "dodger blue", "pale turquoise",
    "dark khaki", "slate blue", "dark slate gray", "lime green", "medium sea green",
    "medium blue", "royal blue", "chocolate", "dark violet", "firebrick", "medium aquamarine",
    "light coral", "light goldenrod", "medium sea green", "navy blue", "cadet blue", "sienna",
    "light salmon", "coral", "thistle", "light sky blue", "medium orchid", "salmon", "dark salmon",
    "medium purple", "dark slate gray", "light sea green", "maroon", "spring green", "gold", "dim gray",
    "green yellow", "lime green", "dark slate blue", "dark goldenrod", "dodger blue", "pale turquoise",
    "dark khaki", "slate blue", "peru"
]

    def update_stickman():
        global x_arm, y_arm, dx_arm, dy_arm, x_text, y_text, dx_text, dy_text, color
        # Clear the right arm on the canvas
        # canvas.delete("right_arm", "text")
        canvas.delete("all")

        # Draw the stickman's arm and text at the new position
        canvas.create_line(100, 80 , x_arm, y_arm, width=2, fill=color[random.randint(0, len(color)-1)], tags="right_arm")  # Right arm
        canvas.create_text(x_text, y_text, text="Coucou twa", fill=color[random.randint(0, len(color)-1)], font=("Arial", 12), tags="text") # Text

        canvas.create_oval(80, 20, 120, 60, width=2, outline=color[random.randint(0, len(color)-1)], fill=color[random.randint(0, len(color)-1)])
        canvas.create_line(100, 60, 100, 160, width=2, fill=color[random.randint(0, len(color)-1)])
        canvas.create_line(100, 80, 60, 120, width=2, fill=color[random.randint(0, len(color)-1)])
        canvas.create_line(100, 160, 60, 240, width=2, fill=color[random.randint(0, len(color)-1)])
        canvas.create_line(100, 160, 140, 240, width=2, fill=color[random.randint(0, len(color)-1)])

        # Update the arm and text positon
        x_arm += dx_arm
        y_arm += dy_arm
        x_text += dx_text
        y_text += dy_text
        

        # Check if stickman's arm is at the top or bottom, reverse direction
        if y_arm < 20 or y_arm > 60:
            dx_arm *= -1
            dy_arm *= -1
        
        # Check if stickman's text is at the top or bottom, reverse direction
        if x_text < 150 or x_text > 160:
            dx_text *= -1
            dy_text *= -1

        # Schedule the next update after a delay
        app.after(50, update_stickman)

    ## Draw usine create_xx with x_start, y_start, x_end_ y_end
    # Draw the head (a circle)
    canvas.create_oval(80, 20, 120, 60, width=2, outline="lime", fill="lime")

    # Draw the body (a line)
    canvas.create_line(100, 60, 100, 160, width=2, fill="green")

    # Draw the left arm (a line)
    canvas.create_line(100, 80, 60, 120, width=2, fill="red")

    # Draw the right arm (a line)
    canvas.create_line(100, 80, 140, 40, width=2, fill="blue", tags="right_arm") # 40 -> 120

    # Draw the left leg (a line)
    canvas.create_line(100, 160, 60, 240, width=2, fill="purple")

    # Draw the right leg (a line)
    canvas.create_line(100, 160, 140, 240, width=2, fill="orange")

    # Add the text "Hello World" next to the head
    canvas.create_text(160, 20, text="Coucou twa", fill="black", font=("Arial", 12), tags="text")

    # Start the animation
    update_stickman()

    # Start the Tkinter main loop
    app.mainloop()
#####

### Packaging ###
## Using Tkinter, add a full game GUI: live score, menu button, time, life bar, inventory, ##
def Game():
    import tkinter as tk

    # Create the main application window
    app = tk.Tk()
    app.title("Game Name")

    # Create a Frame for the game canvas
    game_frame = tk.Frame(app)
    game_frame.pack(fill=tk.BOTH, expand=True)

    # Create a Canvas for the game area
    game_canvas = tk.Canvas(game_frame, width=800, height=600)
    game_canvas.pack(fill=tk.BOTH, expand=True)

    # Create a Label for displaying the score
    score_label = tk.Label(app, text="Score: 0", font=("Helvetica", 16))
    score_label.pack()

    # Create a Label for displaying the time remaining
    time_label = tk.Label(app, text="Time: 60s", font=("Helvetica", 16))
    time_label.pack()

    # Create a progress bar for displaying player's life
    life_bar = tk.Label(app, text="Life:", font=("Helvetica", 16))
    life_bar.pack()

    # Create a Menu bar with game options
    menu_bar = tk.Menu(app)
    app.config(menu=menu_bar)

    # Create a "File" menu with options (e.g., New Game, Save, Load, Exit)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New Game")
    file_menu.add_separator()
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Load")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=app.quit)

    # Create an inventory display (e.g., a listbox or a separate window)

    # Define game functions (e.g., update_score, update_time, start_game, etc.)

    # Define game canvas drawing functions (e.g., draw_character, draw_obstacles, etc.)

    # Implement game logic (e.g., collision detection, scoring, game over conditions, etc.)

    # Implement game loop (update canvas, check game logic, etc.)

    # Start the Tkinter main loop
    app.mainloop()
#####

### Challenge ###
def Challenge(x_sphere=20, y_sphere=20, color="white", sphere_width=130):
    from tkinter import PhotoImage

    # Create the main application window
    app = tk.Tk()
    app.title("Realistic sphere")

    # Create a Frame
    frame = tk.Frame(app)
    frame.pack()

    # Load the background image
    script_dir = os.path.dirname(__file__)
    image_path = os.path.join(script_dir, "sphere.PNG")
    background_image = PhotoImage(file=image_path)
    image_width = background_image.width()
    image_height = background_image.height()

    # Create a Canvas inside the Frame
    canvas = tk.Canvas(frame, width=image_width, height=image_height)
    canvas.pack()

    # canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    # Create a gradient shadow effect
    shadow_x = x_sphere + 50 # X-coordinate of the shadow oval
    shadow_y = y_sphere + 80  # Y-coordinate of the shadow oval
    shadow_height = 70  # Height of the shadow
    num_shadow_layers = 20  # Number of shadow layers (adjust as needed)

    for i in range(num_shadow_layers):
        gray_level = int(255 - (i / num_shadow_layers) * 255)  # Gradually lighter shades of gray
        shadow_color = f'#{gray_level:02x}{gray_level:02x}{gray_level:02x}'  # RGB color from black to white
        # shadow_color = f'#{i*10:02x}{i*10:02x}{i*10:02x}'  # Varying shades of gray
        shadow_width = 210 - i * 3  # Adjust the width based on the layer
        canvas.create_oval(shadow_x, shadow_y, shadow_x + shadow_width, shadow_y + shadow_height,
                            width=0, outline=shadow_color, fill=shadow_color)
    
    # Draw the main sphere
    sphere_num_shadow_layers = 7  # Number of shadow layers (adjust as needed)

    for i in range(sphere_num_shadow_layers):
        gray_level = int((i / sphere_num_shadow_layers) * 255)  # Gradually lighter shades of gray
        sphere_shadow_color = f'#{gray_level:02x}{gray_level:02x}{gray_level:02x}'  # RGB color from black to white
        sphere_shadow_width = sphere_width - i * 5  # Adjust the width based on the layer
        canvas.create_oval(x_sphere, y_sphere, x_sphere + sphere_shadow_width, y_sphere + sphere_width,
                            width=0, outline=sphere_shadow_color, fill=sphere_shadow_color)
    # canvas.create_oval(x_sphere, y_sphere, x_sphere + 130, y_sphere + 130, width=2, outline=color, fill=color)

    # Start the Tkinter main loop
    app.mainloop()

#####
