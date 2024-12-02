import tkinter as tk
from tkinter import messagebox

# Initialize the main application
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")  # Set a fixed window size

# Center everything inside a main frame
main_frame = tk.Frame(root)
main_frame.pack(expand=True)  # Expands the frame to center the content

# Variable to track the game state
current_player = "X"
variable_btn = ["X", "O"]

# Add a label for instructions
label = tk.Label(main_frame, text="Choose one:", font=("Arial", 12))
label.grid(row=0, column=0, padx=5, pady=5)

# Label to display the current player
current_player_label = tk.Label(main_frame, text=f"Current player: {current_player}", fg="blue", font=("Arial", 12))
current_player_label.grid(row=0, column=1, padx=10, pady=5)

# Function to handle button clicks and update the current player
def on_button_click(value):
    global current_player
    current_player = value  # Update the current player
    current_player_label.config(text=f"Current player: {current_player}")  # Update the label

# Create buttons dynamically and place them on the same row
for idx, value in enumerate(variable_btn):
    btn = tk.Button(main_frame, text=value, command=lambda v=value: on_button_click(v), font=("Arial", 12))
    btn.grid(row=0, column=2 + idx, padx=5, pady=5)

# Game board buttons
buttons = [[None, None, None] for _ in range(3)]
# Winning color
winning_color = "lightgreen"

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            highlight_buttons([(row, 0), (row, 1), (row, 2)])
            return True
    # Check columns
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            highlight_buttons([(0, col), (1, col), (2, col)])
            return True
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_buttons([(0, 0), (1, 1), (2, 2)])
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_buttons([(0, 2), (1, 1), (2, 0)])
        return True
    return False

def check_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col]["fg"] = "blue" if current_player == "X" else "red"
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def highlight_buttons(coords):
    for row, col in coords:
        buttons[row][col]["bg"] = winning_color

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for button in row:
            button["text"] = ""
            button["fg"] = "black"
            button["bg"] = "lightgray"

# Create the game grid
game_frame = tk.Frame(main_frame)
game_frame.grid(row=1, column=0, columnspan=4, pady=20)

for i in range(3):
    for j in range(3):
        button = tk.Button(
            game_frame, 
            text="", 
            font=("Arial", 24), 
            width=5, 
            height=2, 
            bg="lightgray",
            fg="black",
            command=lambda i=i, j=j: on_click(i, j)
        )
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Add a reset button
reset_button = tk.Button(main_frame, text="Restart Game", font=("Arial", 14), command=reset_game)
reset_button.grid(row=2, column=0, columnspan=4, pady=10)

# Run the application
root.mainloop()
