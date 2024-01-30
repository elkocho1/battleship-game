# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

"""
 Battleship game
"""

# Global variables
board = [[]]
board.size = 10
num_of_ships = 2
bullets_left = 50
game_over = False
num_of_ships_sunk = 0
ship_positions = [[]]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def check_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """ Check the row and column to place ships there"""
    global board
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

def try_to_place_ship_on_grid(row, col, direction, length):
    """ Based on direction I place a ship on the grid"""
    global board_size

    start_row = row
    end_row = row + 1
    start_col = col
    end_col = col + 1

    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1
    
    elif direction == "right":
        if col + length >= board_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= board_size:
            return False
        end_row = row + length

    return check_grid_and_place_ship(start_row, end_row, start_col, end_col)


def create_board():
    """ Create the grid and randomly place down the ships of different sizes"""
    global board
    global board_size
    global num_of_ships
    global ship_positions

    rows, cols = (board_size, board_size)

    board = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        board.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1
        

def print_board():
    """ Print the board with rows and colums"""

def play():
    print("Welcome to my Battleship game")
    print("Board Size ist 10 x 10 and each player has 8 ships.")
    print("You have in total 50 bullets to take down the enemy ships. Each round the amount will be updated and the hits and misses are getting displayed.")

play()