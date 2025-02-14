import tkinter as tk

# Create the main application window
app = tk.Tk()
app.geometry("300x300")
app.title("Stickman Figure Animated")

# Create a Canvas to draw on
canvas = tk.Canvas(app, width=200, height=300)
canvas.pack()

# Initial position of the stickman's right arm
x_arm, y_arm = 140, 40
dx_arm, dy_arm = 3, 3 # Speed

def update_stickman():
    global x_arm, y_arm, dx_arm, dy_arm
    # Clear the right arm on the canvas
    canvas.delete("right_arm")

    # Draw the stickman's arm and text at the new position
    canvas.create_line(100, 80 , x_arm, y_arm, width=2, fill="blue", tags="right_arm")  # Right arm

    # Update the arm and text positon
    x_arm += dx_arm
    y_arm += dy_arm
    
    # Check if stickman's arm is at the top or bottom, reverse direction
    if y_arm < 20 or y_arm > 60:
        dx_arm *= -1
        dy_arm *= -1

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