# Project Narrative: U.S. State Capitals Game Prototype Request  

<img src = "./assets/learn-nation-logo.webp" alt = "LearnNation Logo" width = "350" height = "auto">

# Project Narrative: U.S. State Capitals Game Prototype

## Introduction

You currently work as a junior developer at **LearnNation**, an innovative company dedicated to building tools that make learning interactive and engaging. Your manager, Sarah, has assigned you your first project: creating an interactive game that helps users memorize the capitals of all 50 U.S. states. Here's the catch—this isn't just a learning tool for fun, but a prototype for a future educational app the company plans to release for schools across the nation.

But not everyone will work on the actual app. You will be chosen based on your knowledge of Python and your ability to work with data types and data structures.

**NOTE:** Your manager Sarah is traditional in her approach to software development. For this project, she wants to assess your ability to code and understand key concepts without the assistance of AI tools. While she recognizes the potential of AI to enhance productivity in the workplace, she believes it's crucial for junior developers to first demonstrate their core skills. As such, she has specifically requested that you don't use AI to create code for this project. This approach allows her to evaluate your fundamental coding abilities and problem-solving skills. You may use AI to get unstuck, but you should write the code on your own. **Make sure you can explain every line of code you write.**

## Project Brief

Sarah provided the following project brief:

> "Our research shows that students struggle to memorize U.S. state capitals, and teachers have asked for a tool to help students learn them in a fun way. We're counting on you to create a game that presents each state one by one, asks the user to guess the capital, and tracks how well they do. We want students to feel motivated by seeing their scores improve, so the app needs to be engaging and clear."

> "The game should shuffle the order of states so it's challenging and give students feedback on whether they guessed correctly. At the end, they'll be able to see their score and decide if they want to play again. Over time, this game will help students remember the capitals of all 50 states more easily."

## Getting Started

Here's how you can get started on the project:

1. **Set up your environment.**
   * Fork and clone the repository provided for you.
   * Once it's cloned, change into the directory and review the starter code located in `lib/script.py`. You'll notice that the list of states and their capitals is already imported for you, so you can jump right into the fun part—building the game logic!

2. **How to Turn off Cursor Auto Complete.** 
   * In the bottom right corner of the screen, hover over the `Cursor Tab` and in the box, choose `Disable Globally`. Also choose `disabled` in the `Cursor Prediction` dropbox. This will enable you to create the code on your own without the help of Cursor. Creating the functions yourself will help you learn the material.
   * If you are completely stuck, you can use Cursor to get unstuck, but **DO NOT** use Cursor to write the entire program. You should use Cursor to get unstuck, but then you should write the code on your own.

3. **Game requirements.**
   * Your program should **prompt the user** to identify the capital of each given state.
   * Keep a **running tally** of how many answers are correct and incorrect.
   * After cycling through all 50 states, the user should be asked whether they want to **play again**.
   * **Hint:** You might want to create a small test list of states and capitals to try out your code before working with all 50 states.

4. **Important features:**
   * The game should not present the states in alphabetical order—use **random.shuffle()** to keep things interesting.
   * Welcome players with a **friendly greeting** when the game starts.
   * Track their score and show them how they're doing after each question.
   * When all 50 states have been covered, **ask the user if they'd like to play again**.

5. **Bonus Features (optional but highly encouraged):**
   * Add a feature to **track how often** each state's capital is guessed correctly or incorrectly.
   * If a player chooses to play again, make the game start with the states they missed the most.
   * Include a **hint feature** that shows the first three letters of the capital for particularly tricky questions.

## Additional Advice

Sarah gives you some additional advice:

> "Remember, this is an educational tool, so clarity is key. Make sure your messages to the user are easy to understand, and don't forget to test your program thoroughly! Also, while it's okay to use tools like Cursor, do not create ai generated code. We want you to deeply understand the code you're writing."

## Conclusion

**Good luck!** Your success with this project will not only help students across the country, but it'll also prove that you're ready to take on even bigger tasks at LearnNation.


**[Project Spec](./project-spec.md)**