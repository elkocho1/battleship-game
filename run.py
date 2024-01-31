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

    def check_hit(self, row, col):
        if self.start_row <= row <= self.end_row and self.start_col <= col <= self.end_col:
            self.hits += 1
            return True
        return False

    def is_sunk(self):
        return self.hits >= (self.end_row - self.start_row + 1) + (self.end_col - self.start_col + 1)

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

    def update_grid(self, row, col, hit):
        if hit:
            self.grid[row][col] = "X"
        else:
            self.grid[row][col] = "#"

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
        self.enemy_board = Board()
        self.tracking_board = Board()
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

        ship = Ship(start_row, end_row, start_col, end_col)
        self.board.place_ship(ship)
        return True

    def get_shot_input(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            try:
                shot = input("Enter row (A-J) and column (0-9) such as A4: ").upper()
                if len(shot) != 2 or not shot[0].isalpha() or not shot[1].isdigit():
                    raise ValueError("Invalid input. Please enter in format A4.")
                row, col = alphabet.index(shot[0]), int(shot[1])
                if row >= self.board.size or col >= self.board.size:
                    raise ValueError("Shot out of range. Please choose within A-J and 0-9.")
                if self.board.grid[row][col] in ["X", "#"]:
                    raise ValueError("You have already shot here. Choose another target coordinate.")
                return row, col
            except ValueError as e:
                print(e)


    def shoot(self, row, col):
        hit = False
        for ship in self.board.ships:
            if ship.check_hit(row, col):
                hit = True
                if ship.is_sunk():
                    self.num_of_ships_sunk += 1
                    print("A ship has been sunk!")
                else:
                    print("Hit!")
                break
        if not hit:
            print("Miss.")
        self.board.update_grid(row, col, hit)
        self.bullets_left -= 1

    def is_game_over(self):
        if self.num_of_ships_sunk == len(self.board.ships):
            print("Congratulations, you have sunk all the ships!")
            return True
        if self.bullets_left <= 0:
            print("Game over. You have run out of bullets.")
            return True
        return False

    def play(self):
        print("Welcome to my Battleship game")
        print("Board Size ist 10 x 10 and each player has 8 ships.")
        print("You have in total 50 bullets to take down the enemy ships. Each round the amount will be updated and the hits and misses are getting displayed.")
        self.place_ships()
        while not self.is_game_over():
            self.board.print_board(debug_mode=False)
            print(f"Bullets left: {self.bullets_left}")
            row, col = self.get_shot_input()
            self.shoot(row, col)

game = Game()
game.play()
