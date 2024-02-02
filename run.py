"""Import the random module for generating random values"""

import random


class Ship:
    def __init__(self, start_row, end_row, start_col, end_col):
        """classificate a ship with its position and hit counts"""
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col
        self.hits = 0

    def check_hit(self, row, col):
        """Check if a ship has been hit at the specified row and column"""
        return self.start_row <= row <= self.end_row and self.start_col <= col <= self.end_col

    def is_sunk(self):
        """Check if a ship is sunk"""
        length = (self.end_row - self.start_row + 1) * (self.end_col - self.start_col + 1)
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

    def place_ship(self, ship):
        """Place ship and mark its position"""
        for r in range(ship.start_row, ship.end_row + 1):
            for c in range(ship.start_col, ship.end_col + 1):
                self.grid[r][c] = "O"
        self.ships.append(ship)

    def update_grid(self, row, col, hit):
        """update the game board grid with X for hits and # for misses"""
        if hit:
            self.grid[row][col] = "X"
        else:
            self.grid[row][col] = "#"
                   
    def print_board(self, hide_ships=True):
        """Print the grid with rows and cols and hiding ships if specified"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print("  " + " ".join(str(i) for i in range(self.size)))
        for row in range(self.size):
            row_display = [self.grid[row][col] if not hide_ships or self.grid[row][col] in ["X", "#"] else "." for col in range(self.size)]
            print(alphabet[row] + " " + " ".join(row_display))
            

class Game:
    def __init__(self):
        """Initialize the game with player, enemy and tracking board and bullet amount"""
        self.player_board = Board()
        self.enemy_board = Board()
        self.tracking_board = Board()
        self.bullets_left = 50

    def place_ships(self, board, num_of_ships=8):
        """Place a specific number of ships randomly on the board"""
        directions = ["left", "right", "up", "down"]
        for i in range(num_of_ships):
            placed = False
            while not placed:
                row, col = random.randint(0, board.size - 1), random.randint(0, board.size - 1)
                direction = random.choice(directions)
                ship_size = random.randint(2, 4)
                placed = self.try_to_place_ship(board, row, col, direction, ship_size)

    def try_to_place_ship(self, board, row, col, direction, length):
        """try to place a ship on the board in a specified direction and length"""
        start_row, end_row = row, row
        start_col, end_col = col, col

        if direction == "left":
            if col - length < 0:
                return False
            start_col = col - length

        elif direction == "right":
            if col + length > board.size:
                return False
            end_col = col + length - 1
        
        elif direction == "up":
            if row - length < 0:
                return False
            start_row = row - length
        
        elif direction == "down":
            if row + length > board.size:
                return False
            end_row = row + length - 1

        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                if board.grid[r][c] == "O":
                    return False

        ship = Ship(start_row, end_row, start_col, end_col)
        board.place_ship(ship)
        return True

    def quit_game(self):
        """quit the game"""
        print("You have chosen to quite the game. Thanks for playing!")
        exit()      

    def get_shot_input(self):
        """Get the players input for a shot"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            try:
                shot = input("Enter row (A-J) and column (0-9) such as A4, or 'Q' to quit the game: \n").upper()
                if shot == "Q":
                    self.quit_game()
                if len(shot) < 2 or len(shot) > 3:
                    raise ValueError("Invalid input length. Please enter in format A4")
                if shot[0] not in alphabet or not shot[1:].isdigit():
                    raise ValueError("Invalid input format. Please enter in format A4")
                row, col = alphabet.index(shot[0]), int(shot[1:])

                if row >= self.enemy_board.size or col >= self.enemy_board.size:
                    raise ValueError("Shot out of range. Please choose within A-J and 0-9.")

                if self.enemy_board.grid[row][col] in ["X", "#"]:
                    raise ValueError("You have already shot here. Choose another target coordinate.")
                return row, col

            except ValueError as e:
                print(e)

    def shoot(self, board, row, col, is_player_shooting=True):
        """Shoot at a specified position on the board and handle hits and misses"""
        hit = False
        ship_sunk = False
        for ship in board.ships:
            if ship.check_hit(row, col):
                hit = True
                ship.hits += 1
                if ship.is_sunk():
                    ship_sunk = True
                break
        if is_player_shooting:
            self.tracking_board.update_grid(row, col, hit)
            self.enemy_board.update_grid(row, col, hit)
        else:
            self.player_board.update_grid(row, col, hit)

        if ship_sunk:
            if is_player_shooting:
                print("You destroyed a ship")
            else:
                print("The enemy destroyed 1 of your ships")

        return hit

    def enemy_turn(self):
        """Simulate the enemys turn by shooting at a random position on the player"""
        row, col = random.randint(0, self.player_board.size - 1), random.randint(0, self.player_board.size - 1)
        print(f"Enemy shoots at ({row}, {col}): ", end="")
        hit = self.shoot(self.player_board, row, col, is_player_shooting=False)
        print("Hit!" if hit else "Miss.")

    def is_game_over(self):
        """Check if the game is over based on bullets left or ship status"""
        if self.bullets_left <= 0:
            print("Game over. You have run out of bullets.")
            return True
        if all(ship.is_sunk() for ship in self.enemy_board.ships):
            print("Congratulations, you have sunk all the ships!")
            return True
        if all(ship.is_sunk() for ship in self.player_board.ships):
            print("Sorry, all your ships have been sunk. Game over!")
            return True
        return False

    def get_player_name(self):
        """Get the players name with validation"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        while True:
            try:
                player_name = input("Please enter your user name: \n")
                if len(player_name) > 20:
                    raise ValueError("Your name cannot be longer than 20 characters! Please try again. ")
                if not all(char in alphabet for char in player_name):
                    raise ValueError("Your name can only include letters and numbers. Please try again. ")
                return player_name
            except ValueError as e:
                print(e)

    def play(self):
        """Start and loop the game"""
        print("Battleship Python Game!")
        print("Board Size ist 10 x 10 and each player has 8 ships.")
        print("You have in total 50 bullets to take down the enemy ships. Each round the amount will be updated and the hits and misses are getting displayed.\n")

        player_name = self.get_player_name()

        self.place_ships(self.player_board)
        self.place_ships(self.enemy_board)

        while not self.is_game_over():
            print(f"\n{player_name}'s Board:")
            self.player_board.print_board(hide_ships=False)
            print("\nComputer Board:")
            self.tracking_board.print_board(hide_ships=True)
            print(f"Bullets left: {self.bullets_left}")

            row, col = self.get_shot_input()
            print(f"You shoot at ({row}, {col}): ", end="")
            if self.shoot(self.enemy_board, row, col, is_player_shooting=True):
                print("Hit!")
            else:
                print("Miss.")
            self.bullets_left -= 1
            
            if not self.is_game_over():
                self.enemy_turn()

"""Call the game when programm runs"""

game = Game()
game.play()
