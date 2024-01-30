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

def play():
    print("Welcome to my Battleship game")
    print("Board Size ist 10 x 10 and each player has 8 ships.")
    print("You have in total 50 bullets to take down the enemy ships. Each round the amount will be updated and the hits and misses are getting displayed.")

play()