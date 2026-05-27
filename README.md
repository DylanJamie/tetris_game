# Tetris in Python (15-Minute Build)

A simple Tetris clone built in Python using Pygame.

This project was built as part of my **"How YOU can code X in 15 minutes"** series on YouTube.

---

## Video Tutorial
https://youtu.be/GWLX08ZdC8c

---

## Features
- Game Matrix and Drawn Matrix
- Imported Files and Organization
- Input arrows with grouped block shapes
- Collision system
- High score system

---

## How It Works
The game is built using a simple game loop:

1. Create the Matrix for the game
2. Allow blocks to constant spwn in and drop
3. group block shapes and colors together 
4. Game over when block collides with new spawn block, check high score file
5. if full row complete add to score 

---

Files
assets/ # all the assets
src/ # all source files
utils.py # Colors, shapes and draw grid function parameters
main.py # main application
high_score_track.txt # highest score achieved

## Requirements
Make sure you have Python installed:

```bash
python --version
