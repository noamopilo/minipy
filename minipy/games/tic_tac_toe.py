import tkinter as tk
import random

def computer():
    if game_over:
        return
    
    empty_tiles = []
    for row in range(3):
        for column in range(3):
            if board[row][column]["text"] == "":
                empty_tiles.append((row, column))
    
    if empty_tiles:
                row, column = random.choice(empty_tiles)
                set_tile(row, column)

def set_tile(row, column):
    global curr_player
    
    if (game_over):
        return
    
    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player
    
    if curr_player == playerO:
        curr_player = playerX
    elif curr_player == playerX:
        curr_player = playerO
    
    if vs_computer and curr_player == playerO:
        label["text"] = "Computer's turn"
    else:
        label["text"] = curr_player+"'s turn"
    
    check_winner()
    
    if not game_over and curr_player == playerO and vs_computer:
        window.after(800, computer)

def check_winner():
    global turns, game_over
    turns += 1
    
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_sea_green)
            for column in range(3):
                board[row][column].config(foreground=color_pine, background=color_sea_green)
            game_over = True
            return
    
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_sea_green)
            for row in range(3):
                board[row][column].config(foreground=color_pine, background=color_sea_green)
            game_over = True
            return
    
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_sea_green)
        for i in range(3):
            board[i][i].config(foreground=color_pine, background=color_sea_green)
        game_over = True
        return
    
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_sea_green)
        board[0][2].config(foreground=color_pine, background=color_sea_green)
        board[1][1].config(foreground=color_pine, background=color_sea_green)
        board[2][0].config(foreground=color_pine, background=color_sea_green)
        game_over = True
        return
    
    if (turns == 9):
        game_over = True
        label.config(text="I'ts a Tie!", foreground=color_sea_green)
        for row in range(3):
            for column in range(3):
                board[row][column].config(foreground=color_pine, background=color_sea_green)
        

def new_game():
    global turns, game_over, curr_player
    
    curr_player = playerX
    turns = 0
    game_over= False
    
    if vs_computer and curr_player == playerO:
        label.config(text="Computer's turn", foreground=color_dark)
    else:
        label.config(text=curr_player+" 's turn", foreground=color_dark)
    
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_dark, background=color_light_blue)

playerX = "X"
playerO = "O"
curr_player = playerX
choice = input("Do you want to play against the computer or another player? (c/p): ").strip().lower()

if choice == "c":
    vs_computer = True
else:
    vs_computer = False

board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

color_light_blue = "#D8F3DC"
color_sea_green = "#40916C"
color_dark_green = "#2D6A4F"
color_pine = "#1B4332"
color_dark = "#081C15"

turns = 0
game_over = False

window = tk.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_light_blue, foreground=color_dark)

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Consolas", 50, "bold"), background=color_light_blue, foreground=color_pine, width=4, height=1, command=lambda row = row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)
        
button = tk.Button(frame, text="RESET", font=("Consolas", 20), background=color_light_blue, foreground=color_dark, command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()