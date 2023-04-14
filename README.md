# Battleship Game 
(Developer: Jeremie Sandot)

![Mockup](docs/mockup/mockup.jpg)

[View live site](https://pp3-battleship.herokuapp.com/)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Owner Goals](#owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [Scope](#scope)
    4. [User Manual](#user-manual)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
    2. [Data Models](#data-models)   
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [Python Validation](#Python-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Goals 

- Develop a Battleship game that can be played on the command line.
- Implement an authentication system using Google Sheets API to allow players to log in. 
- Create a Board class to represent the game board.
- Implement a function to randomly place ships on the computer's grid.
- Create methods to mark the ships on the board, check if a location has a ship, and to fire a shot at a location.

### User Goals
- Authenticate the user with the correct username and password, preventing unauthorized access.
- Play the game of Battleship with a player and a computer, place and track the location of       ships, and mark successful hits and misses on the board.
- Provide user feedback and error messages for invalid inputs or actions, helping the user to understand how to interact with the program correctly.

### Owner Goals
- Provide an engaging and enjoyable gameplay experience: 
- Provide an interface to allow players to log in to the game.
- Allow the player to play against AI

## User Experience

### Target Audience
- Individuals who like board games, strategy games, or games that involve logic and decision-making
- Individuals who are interested in coding.


### User Stories

#### First-time User 
1.	As a new player, I want to be able to sign up so that I can play Battleship.
2.	As a registered player, I want to be able to sign in so that I can start a new game.
3.	As a player, I want to be able to rely on AI to mark my ships on the board so that Improve my skills.
4.	As a player, I want to be able to choose the coordinates so that I can win the game.
5.	As a player, I want to be able to see the result of each turn so that I can keep track of the game.
6.	As a player, I want to be able to choose the size of the board so that I can customize the game.

#### Site Owner
7.	As the game owner, I want to implement a feature that prevents players from entering invalid usernames or passwords to prevent unauthorized access.
8.	As the game owner, I want the application to be user friendly.
9. As a site owner I want the game to be playable on multiple devuices.

### User Manual

#### Overview

- This application is a command-line implementation of the popular game "Battleship". It allows two players, a human and a computer, to play against each other. The game is played on two separate 5x5 grids, one for each player. The grids are initially empty and players take turns firing missiles at each other's grids in an attempt to sink each other's ships.

The application provides the user with prompts and menus to select the game mode, enter their username and password to login, place their ships on their grid, and fire missiles at their opponent's grid. The user can see their own grid and the shots they have made on their opponent's grid. The application also validates input and checks for errors before proceeding to the next step. The game ends when one of the players has sunk all of the ships of their opponent.

#### Main Menu

- On the main menu you will be provided with 2 options

1. Sign In : this option is for already registered users. Upon validation of their credentilas (username and password ) a user gains access to the application.

2. Sign up : This option allows a user who has never played this game to create a username and a password. 

#### Sign In Option

- If a user selects the option 1 "Sign in" in the battlefield game, the login function will be called. The user will be prompted to enter their username and password. 

- The function will first validate that the username and password are not empty and have at least 5 characters. 

- Then, it will authenticate with Google Sheets using the authenticate function, and retrieve the auth_dict worksheet. It will retrieve all rows in the worksheet as a list of dictionaries, and check if there's a row with the given username and password. 

- If the username and password match, the function will return True, indicating that the user has successfully signed in. 
- If the username and password don't match, the function will return False, indicating that the sign in failed.

#### Sign up Option
- The signup operation is used to create a new account on the system. In order to sign up, the user will need to provide a unique username and a password that meets certain requirements, such as being at least 5 characters long.
- When the user selects option 2 he is required to enter a username with minimum 5 characters
- if the user fails to meet the 5 charracter minimum they will get an error message (must be at least 5 characters)
- if the user tries to enter a blank username a warning will indicate that a username cannot be blank
- if the user meets all the criteria he is prompted to enter a password with at least 5 characters
- if the password is < 5 characters or baknk he gets a warning ( invalid password must be at least 5 characters )

### Game Page

- Upon sucessfull sign in the user is prompted to select 3 board sizes
    - 5x5
    - 6x6
    - 7x7 


## Technical Design

### Flowchart

The following flowchart summarises the structure and logic of the application.

<details><summary>Flowchart</summary>
<img src="docs/flowchart/flowchart.jpg">
</details>


### Data models
- The data model used in the code consists of two classes, Board and Player.

- The Board class is responsible for initializing the game board, placing ships on the board, firing shots at the opponent's board, and displaying the game board to the user. The Board class has the following attributes:
    - size
    - grid
    - ships
    - computer_ships
    - player_name
    - board_type

- The Board class has the following methods:

    - __init__(self, size, player_name, board_type): initializes the Board object.
    - __str__(self): returns a string representation of the board, which is printed when the board needs to be displayed.
    - mark_ship(self, x, y): adds a ship at a given position on the board.
    place_computer_ships(self): randomly places ships on the computer's board.
    - has_ship(self, x, y): returns True if there is a ship at a given position on the board.
    - is_valid(self, x, y): returns True if the given position is valid on the board.
    - fire(self, x, y): returns True if there is a ship at a given position on the board, otherwise False.
    - get_grid_coords(self, x, y): converts coordinates from the shot_grid to the grid.

- The Player class is responsible for the game logic and interaction with the user. The Player class has the following attributes:

    - board: a Board object representing the user's board.
    - shot_grid: a 2D list representing the user's shots on the computer's board.

- The Player class has the following methods:

    - __init__(self, size, player_name): initializes the Player object.
    - setup_board(self): prompts the user to mark their ships on the board.
    - play(self, computer_board): allows the user to play against the computer.

- Google sheets API.  JUSTIFICATION: I have chosen to use Google Sheets API so that the required data for the app will persist outside of the container.


## Technologies Used

### Languages

- [Python 3](https://www.python.org/)

### Frameworks and Tools

1. [Git](https://git-scm.com/) - Git was used for version control to push the code to GitHub.
2. [GitHub](https://github.com/) - GitHub was used as a remote repository to store project code. 
5. [Google Sheets](https://www.google.co.uk/sheets/about/) - was used to store data outside of the program.  The vehicle catalogue and appraisal data stored in 2 separate sheets.
6. [Google Cloud Platform](https://cloud.google.com/cloud-console/) - was used to manage access and permissions to the google services, google auth, sheets etc.
7. [Heroku](https://www.heroku.com/about) - Was used to deploy, manage, and scale this apps.
8. [Diagrams.net](https://app.diagrams.net/) was used to draw program flowchart

### Libraries

#### Python Libraries
- random - used to alternate first player to start the game

#### Third Party Libraries
- [colorama](https://pypi.org/project/colorama/) - JUSTIFICATION: To add color to the terminal and enhance user experience. 
- [gspread](https://docs.gspread.org/en/latest/) - JUSTIFICATION: I used gspread to add and manipulate data in my Google spreadsheet and to interact with Google APIs
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) - JUSTIFICATION: module used to set up the authentification needed to access the Google API and connect my Service Account with the Credentials function.

## Features

### Main menu

Visualy pleasant welcome screen, Interactive Menu Prompt the user to either signup or sign in 
user story covered 1,2,7
<details><summary>Main Menu</summary>
<img src="docs/features/main_menu.jpg">
</details>

### Sign Up
Function to create new user's login credentials and saving them on the "auth_dict" worksheet. 
User stories covered 1,7
<details><summary>Sign Up</summary>
<img src="docs/features/main_menu.jpg">
</details>

### Sign In
Function to validate the user's login credentials using the "auth_dict" worksheet. 
User stories covered 2,7
<details><summary>Sign Up</summary>
<img src="docs/features/main_menu.jpg">
</details>

### Input Validation
Provides Feed back to the user : After user is logged in successfully, a welcome message is displayed
User story covered 7
<details><summary>Input Validation</summary>
<img src="docs/features/input_validation.jpg">
</details>

### Greetings
Personalised Greeting: The login phase has been sucessuful. The player is welcomed gy his own name. the system provides feedBack for ease of use.
User story covered 9
<details><summary>Greetings</summary>
<img src="docs/features/greetings1.jpg">
</details>

### Select Board Size
In order to prevent the game from behing too large or too small the game has 3 different predefined sixes and input validation.
User story covered 6,8
<details><summary>Board Size.jpg</summary>
<img src="docs/features/board_size.jpg">
</details>

### Playing against AI
I want to improve my skills therefore I relay on the randomness of the ship placement to improve my skills
user story covered 3
<details><summary>AI_generated.jpg</summary>
<img src="docs/features/board_size.jpg">
</details>

### choose my coordintes
I want to be able to choose the coordinates of my oponent's ships location. I want the system to tell me when the coordinates that I have choses hav been slected before. I also want the system to tell me when my selection is out of bounds or the selection is illegal.
user story covered 4
<details><summary>AI_generated.jpg</summary>
<img src="docs/features/coordinates.jpg">
</details>

### Feedback and user friendliness
At any stage of the game the player is provided with immediate feedback. The player can therefore keep track of score and generalyy what is happening in the game. I wan tehe game to be playable on various device sizes
User story covered 5,9
<details><summary>feedback.jpg</summary>
<img src="docs/features/feedback.jpg">
</details>
<details><summary>results.jpg</summary>
<img src="docs/features/won.jpg">
</details>
<details><summary>Multi Platform.jpg</summary>
<img src="docs/features/responsiveness.jpg">
</details>

## Testing

### Python

The code passes the python validator with no error.

<details><summary>Validation</summary>
<img src="docs/validation/python_validation.jpg">
</details>

### Testing user stories

1. As a new player, I want to be able to sign up so that I can play Battleship.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main screen |      Select option 2       | User is prompted to enter a username and password | Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/story1.jpg">
</details>

2. As a registered player, I want to be able to sign in so that I can start a new game.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main screen |      Select option 1       | User is prompted to enter a username and password | Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/story2.jpg">
</details>

3.  As a player, I want to be able to rely on AI to mark my ships on the board so that Improve my skills.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Screen |Player is informed that the AI has placed the compute ships on the computer board      | ships placed | Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/story3.jpg">
</details>

4.  As a player, I want to be able to choose the coordinates so that I can win the game.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Screen |Player is informed that the AI has placed the compute ships on the computer board| ships placed | Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/story4a.jpg">
</details>

5.  As a player, I want to be able to see the result of each turn so that I can keep track of the game.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Screen |Player makes his selection and validates| computer tells results| Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/story5.jpg">
</details>


6.  As a player, I want to be able to choose the size of the board so that I can customize the game.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Screen |Player is informed that the AI has placed the compute ships on the computer board      | ships placed | Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/story6.jpg">
</details>

7.  As the game owner, I want to implement a feature that prevents players from entering invalid usernames or passwords to prevent unauthorized access.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main screen |Player is prompted to input credentials| if username or password blank or doen't meet the lenght criteria (for signup) it will be rejected| Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/story7.jpg">
</details>



8.  As the game owner, I want the application to be user friendly.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Screen |there is clear choice 1 or 2 | Input validation so not to confuse the player | Works as expected |
| login|whether you sign up or sign in everything is clear | Input validation so not to confuse the player | Works as expected |
| Game phase|there is input validation at every phase of the game| the player is never second guessing | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/story8a.jpg">
<img src="docs/testing/story8b.jpg">
</details>

9. As a site owner I want the game to be playable on multiple devices.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game ara |testing the game on multiple devices | games adapt to the resolution of the device | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/story8a.jpg">
</details>


## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| 'When the player hits an enemy ship the system displays corodinates already taken |   Not fixed - made many changes did not have enough time  |

## Deployment

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository 

Forking this GitHub repository allows you to make a copy of the original to view or make changes without affecting the original. You can do this by following these steps...

1. Log into your GitHub account and find the [repository](https://github.com/bwogit/PP3_BATTLE).
2. Click 'Fork' (last button on the top right of the repository page).
3. You will then have a copy of the repository in your own GitHub account. 

### Making a Local Clone

1. Log into your GitHub account and find the [repository](https://github.com/bwogit/PP3_BATTLE).
2. Click on the 'Code' button (next to 'Add file'). 
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Then open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. In your IDE's terminal type 'git clone' followed by the URL you copied.
7. Press Enter. 
8. Your local clone will now be made.

## Credits

### Code

- **Code Institute** - for git template IDE and heroku deployment instructions. but also for the general presentation of the game battleship this project is a variation of. 
- Code Institute - for git template IDE and "Love Sandwiches - Essentials Project" which helped me with connecting the Google Spreadsheet to my project.
- **Google** - for library [gspread](https://docs.gspread.org/en/latest/) and [APIS](https://developers.google.com/sheets/api)
- How to install a Python module, eg. [email validation](https://pypi.org/project/email-validator/Installing)
- [Stack overflow](https://stackoverflow.com/questions/75934801/simplifying-code-for-placing-ships-in-battleship-game-in-python-and-conducting-u) o help me undertsand random
-[youtube](https://www.youtube.com/)
- I was visually inspired by a couple of projects that i saw in the internet
- Though various sources on the internet provided explainations and examples, the code was put together and tested by me.

## Acknowledgements
- Thank you Mo for yout professional guidance, words of encouragement and support!
-- Code Institute community on Slack for resources and support
