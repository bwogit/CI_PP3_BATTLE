# Battleship Game 
(Developer: Jeremie Sandot)

![Mockup FMS](docs/mockup/mockup.jpg)

[View live site](https://pp3-battleship.herokuapp.com/)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
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

### User Goals
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
3.	As a player, I want to be able to rely on AI to mark my ships on the board so that I can start the game.
4.	As a player, I want to be able to fire missiles at my opponent's board so that I can win the game.
5.	As a player, I want to be able to see the result of each turn so that I can keep track of the game.

#### Site Owner
1.	As the game owner, I want to implement a feature that prevents players from entering invalid usernames or passwords to prevent unauthorized access.
2.	As the game owner, I want to implement a feature that prevents players from entering board sizes that are too small or too large to ensure that the game is fair and playable.
3.	As the game owner, I want to implement a feature that prevents players from placing ships on top of each other to ensure that the game is fair and playable.
5.	As the game owner, I want to implement a feature that allows players to play against a computer AI so that they can practice and improve their skills.

### User Manual

#### Overview

- This application is a command-line implementation of the popular game "Battleship". It allows two players, a human and a computer, to play against each other. The game is played on two separate 5x5 grids, one for each player. The grids are initially empty and players take turns firing missiles at each other's grids in an attempt to sink each other's ships.

The application provides the user with prompts and menus to select the game mode, enter their username and password to login, place their ships on their grid, and fire missiles at their opponent's grid. The user can see their own grid and the shots they have made on their opponent's grid. The application also validates input and checks for errors before proceeding to the next step. The game ends when one of the players has sunk all of the ships of their opponent.
