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