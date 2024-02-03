# Battleship Game

![Responsive Mock Up](documentation/mock-up-responsive.png)

The game is a Python terminal project whose primary purpose is to have fun and play it.

Users the classic battleship game and try to win against the computer. In total you play 50 rounds max, and u have to sunk 8 ships from the enemy. 

---

## How to play: 

1. Open the game with this URL: https://michaels-battleship-game-d48b393c746c.herokuapp.com/ in your browser
2. As soon as the page is loaded, click "Run Program".
3. Introduce yourself to the program. 
4. Now see your board and the computer board.
5. Enter your shot coordinates.
6. Play as many round as u finish.

---

## User Stories
### First Time Visitor Goals

* As a First Time Visitor, I want to quickly understand the program's primary purpose so that I can learn more about this program.
* As a First Time Visitor, I want to navigate through the program easily so that I can find the content.
* As a First Time Visitor, I want to find the program useful for myself so that I can fulfill my expectations.


### Frequent Visitor Goals:

* As a Frequent User, I want to be able to win the game and use it on my phone.
* As a Frequent User, I want the game to be difficult. 

---

## Features

**When the program is loaded**

* The user can see a welcoming message which engages to start playing and the polite question to enter the user name:

![Welcome to the game](documentation/features-welcome.png)

* When the user enters its name, the game shows the 2 players board. 
* On the player board the player can see the location of its ships.
* On the computers board the player only sees the water marks
* Futher more the player can see the amount of bullets. 
* Last but not least the input field to place the shot coordinates. 
* Input validation and error checking
    * You cannot enter coordinates outside the size of the grid
    * You must enter in a specific format like A4
    * You cannot enter the same coordinates twice
![Error Messages](documentation/error-message.png)
* After each shot input the shot will be displayed on either the player board or enemy board.
* Each shot represents either a hit "X" or a miss "#".
![Hits and Miss](documentation/hits-miss.png)
* As soon as the game is over the player reseaves a message that all the bullets are out.
* Furthermore, the amounts of ships that the player and the computer sunk are displayed. 
![End-Message](documentation/end-message.png)
* After this message, the player can choose to quit the game or restart the game.
* "No" will exit the game and leave a thank you message.
* "Yes" will restart the game

---

## Technologies Used

### Languages:

- [Python 3.12.1](https://www.python.org/downloads/release/python-3121/): used to anchor the project and direct all application behavior

### Frameworks/Libraries, and Tools:
#### Python modules:

##### Standard library imports:
- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random number generation.
- [os](https://docs.python.org/3/library/os.html ) was used to clear the terminal before and after running the program.

##### Third-party imports:
- None.

#### Other tools:
- [Codeanywhere](https://codeanywhere.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [Canva](https://www.canva.com/) was used to make and resize images for the README file.
- [Heroku](https://www.heroku.com/) was used to deploy the project.

