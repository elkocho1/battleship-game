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
        return self.start_row <= row <= self.end_row and self.start_col <= col <= self.end_col
        

    def is_sunk(self):
        length = (self.end_row - self.start_row + 1) + (self.end_col - self.start_col + 1)
        return self.hits == length

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
            if self.grid[row][col] != "X":
                self.grid[row][col] = "#"
                   

    def print_board(self, hide_ships=True):
        """Print the grid with rows and cols"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for row in range(self.size):
            print(alphabet[row], end=") ")
            for col in range(self.size):
                cell = self.grid[row][col]
                if cell == "O" and hide_ships:
                    print(".", end=" ")
                else:
                    print(cell, end=" ")
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
        

    #add methods for game loop, shooting and game over

    def place_ships(self, board, num_of_ships=8):
        """Place a specific number of ships randomly on the board"""
        directions = ["left", "right", "up", "down"]
        for i in range(num_of_ships):
            placed = False
            while not placed:
                row, col = random.randint(0, 9), random.randint(0, 9)
                direction = random.choice(directions)
                ship_size = random.randint(3, 5)
                placed = self.try_to_place_ship(board, row, col, direction, ship_size)

    def try_to_place_ship(self, board, row, col, direction, length):
        """try to place a ship on the board in a specified direction and length"""
        start_row, end_row = row, row
        start_col, end_col = col, col

        if direction == "left":
            if col - length < 0:
                return False
            start_col = col - length + 1

        elif direction == "right":
            if col + length > board.size:
                return False
            end_col = col + length - 1
        
        elif direction == "up":
            if row - length < 0:
                return False
            start_row = row - length + 1
        
        elif direction == "down":
            if row + length > board.size:
                return False
            end_row = row + length - 1

        ship = Ship(start_row, end_row, start_col, end_col)
        board.place_ship(ship)
        return True

    def get_shot_input(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            try:
                shot = input("Enter row (A-J) and column (0-9) such as A4: ").upper()
                if len(shot) != 2 or not shot[0].isalpha() or not shot[1].isdigit():
                    raise ValueError("Invalid input. Please enter in format A4.")
                row, col = alphabet.index(shot[0]), int(shot[1])
                if row >= self.enemy_board.size or col >= self.enemy_board.size:
                    raise ValueError("Shot out of range. Please choose within A-J and 0-9.")
                if self.enemy_board.grid[row][col] in ["X", "#"]:
                    raise ValueError("You have already shot here. Choose another target coordinate.")
                return row, col
            except ValueError as e:
                print(e)


    def shoot(self, board, row, col, is_player_shooting=True):
        hit = False
        ship_present = False
        for ship in board.ships:
            if ship.check_hit(row, col):
                hit = True
                ship_present = True
                break
        if is_player_shooting:
            board.update_grid(row, col, hit, False)
        else:
            board.update_grid(row, col, hit, ship_present)
        return hit

    def enemy_turn(self):
        row, col = random.randint(0, 9), random.randint(0, 9)
        print(f"Enemy shoots at ({row}, {col}): ", end="")
        hit = self.shoot(self.player_board, row, col, False)
        print("Hit!" if hit else "Miss.")

    def is_game_over(self):
        sunk_ships = sum(1 for ship in self.enemy_board.ships if ship.is_sunk())
        if sunk_ships == len(self.enemy_board.ships):
            print("Congratulations, you have sunk all the ships!")
            return True
        if self.bullets_left <= 0:
            print("Game over. You have run out of bullets.")
            return True
        if all(ship.is_sunk() for ship in self.enemy_board.ships):
            print("Congratulation, you have sunk all the ships!")
            return True
        return False

    def play(self):
        print("Welcome to my Battleship game")
        print("Board Size ist 10 x 10 and each player has 8 ships.")
        print("You have in total 50 bullets to take down the enemy ships. Each round the amount will be updated and the hits and misses are getting displayed.")
        self.place_ships(self.player_board)
        self.place_ships(self.enemy_board)

        while not self.is_game_over():
            print("\nYour Board:")
            self.player_board.print_board(hide_ships=False)
            print("\nTracking Board:")
            self.tracking_board.print_board(hide_ships=True)
            print(f"Bullets left: {self.bullets_left}")

            row, col = self.get_shot_input()
            print(f"You shoot at ({row}, {col}): ", end="")
            if self.shoot(self.tracking_board, row, col):
                print("Hit!")
            else:
                print("Miss.")
            self.bullets_left -= 1
            
            if not self.is_game_over():
                self.enemy_turn()

game = Game()
game.play()
