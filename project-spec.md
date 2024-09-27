# U.S. State Capitals Game - Project Specification

## 1. Project Overview

### 1.1 Project Name
U.S. State Capitals Learning Game

### 1.2 Project Description
Develop an interactive educational game to help students memorize the capitals of all 50 U.S. states. This game will serve as a prototype for a future educational app to be released for schools across the nation.

### 1.3 Project Objectives
- [ ] Create an engaging and interactive learning experience
- [ ] Improve students' knowledge of U.S. state capitals
- [ ] Provide a tool for teachers to supplement their geography lessons

## 2. Functional Requirements

### 2.1 Core Game Mechanics
- [ ] Present each U.S. state to the user one by one
- [ ] Prompt the user to input the capital for each state
- [ ] Provide immediate feedback on the correctness of each answer
- [ ] Track and display the user's score throughout the game
- [ ] Shuffle the order of states for each playthrough
- [ ] Offer the option to play again after completing all 50 states

### 2.2 User Interface
- [ ] Display a welcome message and game instructions at the start
- [ ] Show the current state and prompt for its capital
- [ ] Present the user's current score after each question
- [ ] Display the final score at the end of the game
- [ ] Provide a clear option to play again or exit the game

### 2.3 Scoring System
- [ ] Maintain a running tally of correct and incorrect answers
- [ ] Calculate and display a final score (e.g., percentage or X out of 50)

### 2.4 Data Management
- [ ] Utilize the provided list of states and their capitals
- [ ] Implement random shuffling of the state order for each game session

## 3. Technical Specifications

### 3.1 Development Environment
- Language: Python
- File Structure:
  - Main game logic in `lib/script.py`
  - Starter code and state/capital data provided

### 3.2 Key Functions (Suggested)
- `shuffle_states()`: Randomize the order of states
- `display_question(state)`: Show the current state to the user
- `get_user_input()`: Prompt and receive user's guess
- `check_answer(user_input, correct_capital)`: Verify the user's answer
- `update_score(is_correct)`: Modify the user's score
- `display_score()`: Show current or final score
- `play_again()`: Ask if the user wants to restart the game

## 4. Optional Enhancements

### 4.1 Answer Tracking
-  [ ] Record the frequency of correct/incorrect answers for each state
- [ ] Prioritize frequently missed states in subsequent playthroughs

### 4.2 Hint System
- [ ] Implement a feature to reveal the first three letters of the capital for difficult questions

### 4.3 Difficulty Levels
- [ ] Easy: Show multiple choice options
- [ ] Medium: Standard input with hint availability
- [ ] Hard: No hints, stricter spelling requirements


## 5. Deliverables

- Fully functional Python script (`lib/script.py`)
- README file with setup and running instructions
- Brief documentation of code structure and any third-party libraries used

## 6. Timeline

- Development: 3 days
- Testing and Refinement: 1 day
- Final Submission: Monday at 2pm

## 7. Additional Notes

- Prioritize code readability and maintainability
- Comment code thoroughly for future reference
- While external tools (e.g., Cursor) can be used for assistance. However, **do not create ai generated code.**

**[Instructions for Project](./readme.md)**



