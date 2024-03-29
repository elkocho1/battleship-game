"""Import the random module for generating random values"""

import random
import os


class Ship:
    """
    Represents a ship in the game with a specific position on the board.

    Attributes:
        start_row (int): The starting row of the ship on the board.
        end_row (int): The ending row of the ship on the board.
        start_col (int): The starting column of the ship on the board.
        end_col (int): The ending column of the ship on the board.
        hits (int): The number of hits the ship has taken.

    Methods:
        check_hit(row, col): Returns True if the given row and
        column hit the ship.
        is_sunk(): Returns True if the ship is sunk (hits equal to its size).
    """
    def __init__(self, start_row, end_row, start_col, end_col):
        """classificate a ship with its position and hit counts"""
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col
        self.hits = 0

    def check_hit(self, row, col):
        """Check if a ship has been hit at the specified row and column"""
        return (
            self.start_row <= row <= self.end_row and
            self.start_col <= col <= self.end_col
        )

    def is_sunk(self):
        """Check if a ship is sunk"""
        length = (
            (self.end_row - self.start_row + 1) *
            (self.end_col - self.start_col + 1)
        )
        return self.hits == length


class Board:
    """
    Represents the game board in the game, holding ships and tracking shots.
    Attributes:
        size (int): The size of the game board (number of rows and columns).
        grid (list of lists): The game board grid, representing ship
        positions and shot results.
        ships (list): A list of Ship objects placed on the board.
    Methods:
        place_ship(ship): Places a ship on the board.
        update_grid(row, col, hit): Updates the grid based on shot
        results (hit or miss).
        print_board(hide_ships=True): Prints the board to the console,
        optionally hiding ships.
    """
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
            row_display = [
                self.grid[row][col] if not hide_ships or self.grid[row][
                    col
                ] in ["X", "#"] else "." for col in range(self.size)
            ]
            print(alphabet[row] + " " + " ".join(row_display))


class Game:
    """
    Manages the game, including setting up the board, handling player input,
    and executing the game loop.

    Attributes:
        player_board (Board): The player's game board.
        enemy_board (Board): The enemy's (computer's) game board.
        tracking_board (Board): Used by the player to track shots
        against the enemy.
        bullets_left (int): The number of shots the player has remaining.
        player_ships_sunk (int): The number of enemy ships sunk by the player.
        enemy_ships_sunk (int): The number of player's ships sunk by the enemy.

    Methods:
        place_ships(board, num_of_ships): Randomly places
        ships on the given board.
        try_to_place_ship(board, row, col, direction, length):
        Attempts to place a ship on the board.
        quit_game(): Exits the game.
        get_shot_input(): Gets the player's shot input.
        shoot(board, row, col, is_player_shooting):
        Processes a shot at the given position.
        enemy_turn(): Simulates the enemy's turn.
        is_game_over(): Checks if the game is over.
        get_player_name(): Gets the player's name with validation.
        ask_play_again(): Asks the player if they want to play again.
        play(): Starts and manages the game loop.
    """

    def __init__(self):
        """
        Initialize the game with player, enemy and tracking board
        and bullet amount
        """
        self.player_board = Board()
        self.enemy_board = Board()
        self.tracking_board = Board()
        self.bullets_left = 50
        self.player_ships_sunk = 0
        self.enemy_ships_sunk = 0

    def place_ships(self, board, num_of_ships=8):
        """Place a specific number of ships randomly on the board"""
        directions = ["left", "right", "up", "down"]
        for i in range(num_of_ships):
            placed = False
            while not placed:
                row, col = (
                    random.randint(0, board.size - 1),
                    random.randint(0, board.size - 1)
                )
                direction = random.choice(directions)
                ship_size = random.randint(2, 4)
                placed = self.try_to_place_ship(
                    board,
                    row,
                    col,
                    direction,
                    ship_size
                )

    def try_to_place_ship(self, board, row, col, direction, length):
        """
        try to place a ship on the board in
        a specified direction and length
        """
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
        self.clear_screen()
        print("You have chosen to quite the game. Thanks for playing!")
        exit()

    def get_shot_input(self):
        """Get the players input for a shot"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            try:
                shot = input(
                    "\nEnter row (A-J) and column (0-9) such as A4," +
                    " or 'Q' to quit the game: \n"
                ).upper()
                if shot == "Q":
                    self.quit_game()
                if len(shot) < 2 or len(shot) > 3:
                    raise ValueError(
                        "Invalid input length. Please enter in format A4"
                    )
                if shot[0] not in alphabet or not shot[1:].isdigit():
                    raise ValueError(
                        "Invalid input format. Please enter in format A4"
                    )
                row, col = alphabet.index(shot[0]), int(shot[1:])

                if (
                    row >= self.enemy_board.size or
                    col >= self.enemy_board.size
                ):
                    raise ValueError(
                        "Shot out of range. Please choose within A-J and 0-9."
                    )

                if self.enemy_board.grid[row][col] in ["X", "#"]:
                    raise ValueError(
                        "You have already shot here." +
                        " Choose another target coordinate."
                    )
                return row, col

            except ValueError as e:
                print(e)

    def shoot(self, board, row, col, is_player_shooting=True):
        """
        Shoot at a specified position on the board and handle hits and misses
        """
        hit = False
        ship_sunk = False
        for ship in board.ships:
            if ship.check_hit(row, col):
                hit = True
                ship.hits += 1
                if ship.is_sunk():
                    ship_sunk = True
                    if is_player_shooting:
                        self.player_ships_sunk += 1
                    else:
                        self.enemy_ships_sunk += 1
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
        """
        Simulate the enemys turn by shooting at a random
        position on the player
        """
        row, col = (
            random.randint(0, self.player_board.size - 1),
            random.randint(0, self.player_board.size - 1)
        )
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
        alphabet = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        )
        while True:
            try:
                player_name = input("Please enter your user name: \n").strip()
                if not player_name:
                    raise ValueError(
                        "Your name cannot be empty or use spaces!" +
                        " Please try again. "
                    )
                if len(player_name) > 20:
                    raise ValueError(
                        "Your name cannot be longer than 20 characters!" +
                        " Please try again. "
                    )
                if len(player_name) < 1:
                    raise ValueError(
                        "Your name must contain at least 1 characters!" +
                        " Please try again. "
                    )
                if not all(char in alphabet for char in player_name):
                    raise ValueError(
                        "Your name can only include letters and numbers." +
                        " Please try again. "
                    )
                return player_name
            except ValueError as e:
                print(e)

    def ask_play_again(self):
        response = input(
            "Would you like to play again (yes/no)? \n"
        ).strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid input. Please answer 'yes' or 'no'. ")
            return self.ask_play_again()

    def clear_screen(self):
        """Clear te screen"""
        if os.name == "nt":
            _ = os.system("cls")
        else:
            _ = os.system("clear")

    def play(self):
        """Start and loop the game"""
        while True:
            welcome_message = (f"""
Welcome to Battleship Python Game!
Board Size ist 10 x 10 and each player has 8 ships.
You have in total 50 bullets to take down the enemy ships.
Each round the amount will be updated and the hits and misses are getting
displayed.
This is the legend:
- # means Miss!
- X means Hit!
- . means Water!
- O are your ships!
            """)
            print(welcome_message)

            player_name = self.get_player_name()
            self.clear_screen()
            self.player_board = Board()
            self.enemy_board = Board()
            self.tracking_board = Board()
            self.bullets_left = 50
            self.player_ships_sunk = 0
            self.enemy_ships_sunk = 0

            self.place_ships(self.player_board)
            self.place_ships(self.enemy_board)

            while not self.is_game_over():

                print(f"\n{player_name}'s Board:")
                self.player_board.print_board(hide_ships=False)
                print("\nComputer Board:")
                self.tracking_board.print_board(hide_ships=True)
                print(f"\nBullets left: {self.bullets_left}")

                if self.bullets_left > 0:
                    row, col = self.get_shot_input()
                    print("-----------------------------------------")
                    print(f"\nYou shoot at ({row}, {col}): ", end="")
                    if self.shoot(
                        self.enemy_board, row, col, is_player_shooting=True
                    ):
                        print("Hit!")
                    else:
                        print("Miss.")
                    self.bullets_left -= 1

                if self.bullets_left >= 0:
                    self.enemy_turn()

            print(f"\n{player_name}'s Final Board:")
            self.player_board.print_board(hide_ships=False)
            print("\nComputers Final Board:")
            self.tracking_board.print_board(hide_ships=True)
            if self.bullets_left <= 0:
                print("Game over.You have used your last bullet \n")
            if all(ship.is_sunk() for ship in self.enemy_board.ships):
                print("Congratulations, you have sunk all the ships! \n")
            elif all(ship.is_sunk() for ship in self.player_board.ships):
                print("Sorry, all your ships have been sunk. Game over! \n")
            else:
                print(f"""
You sunk {self.player_ships_sunk} of the enemys ships.
                """)
                print(f"""
The enemy sunk {self.enemy_ships_sunk} of your ships
                """)

            if not self.ask_play_again():
                print("Thanks for playing! Exiting the game now...")
                self.clear_screen()
                print("Thank you for being with us!")
                break
            else:
                print("Restarting now ....")


if __name__ == "__main__":
    """Call the game when programm runs"""
    game = Game()
    game.play()
    