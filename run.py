# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

"""
 Battleship game

"""

class Ship:
    def __init__(self, start_row, end_row, start_col, end_col):
        """classificate a ship with its position and hit counts"""
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col
        self.hits = 0

    def is_sunk(self):
        return self.hits == self.size

class Board:
    def __init__(self, size=10):
        """initialize the board with a given size"""
        self.size = size
        self.grid = []
        for row in range(size):
            row_data = []
            for col in range(size):
                row_data.append(".")
            self.grid.append(row_data)
        self.ships = []

    #add methods for placing ships, checking hits

    def place_ship(self, ship):
        """Place ship and mark its position"""
        for r in range(ship.start_row, ship.end_row + 1):
            for c in range(ship.start_col, ship.end_col + 1):
                self.grid[r][c] = "O"
        self.ships.append(ship)

    def print_board(self, debug_mode=False):
        """Print the grid with rows and cols"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for row in range(self.size):
            print(alphabet[row], end=") ")
            for col in range(self.size):
                if self.grid[row][col] == "O" and not debug_mode:
                    print(".", end=" ")
                else:
                    print(self.grid[row][col], end=" ")
            print("")

        print("  ", end=" ")
        for i in range(self.size):
            print(str(i), end=" ")
        print("")

class Game:
    def __init__(self):
        self.player_board = Board()
        self.bullets_left = 50
        self.num_of_ships_sunk = 0

    #add methods for game loop, shooting and game over

    def place_ships(self, num_of_ships=8):
        """Place a specific number of ships randomly on the board"""
        directions = ["left", "right", "up", "down"]
        for i in range(num_of_ships):
            placed = False
            while not placed:
                row, col = random.randint(0, 9), random.randint(0, 9)
                direction = random.choice(directions)
                ship_size = random.randint(3, 5)
                placed = self.try_to_place_ship(row, col, direction, ship_size)

    def try_to_place_ship(self, row, col, direction, length):
        """try to place a ship on the board in a specified direction and length"""
        start_row, end_row = row, row
        start_col, end_col = col, col

        if direction == "left":
            if col - length < 0:
                return False
            start_col = col - length + 1

        elif direction == "right":
            if col + length > self.board.size:
                return False
            end_col = col + length - 1
        
        elif direction == "up":
            if row - length < 0:
                return False
            start_row = row - length + 1
        
        elif direction == "down":
            if row + length > self.board.size:
                return False
            end_row = row + length - 1

        


    def play(self):
        print("Welcome to my Battleship game")
        print("Board Size ist 10 x 10 and each player has 8 ships.")
        print("You have in total 50 bullets to take down the enemy ships. Each round the amount will be updated and the hits and misses are getting displayed.")
        self.place_ships()

game = Game()
game.play()
