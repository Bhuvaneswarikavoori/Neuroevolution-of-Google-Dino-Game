# Neuroevolution of Dino Game

This project is an implementation of the Google Dino Game using Python, Pygame, and the NEAT (NeuroEvolution of Augmenting Topologies) algorithm. The objective is to train an AI agent to play the game and avoid obstacles by learning to jump over cacti.

## Prerequisites

To run this project, you need to have Python 3.6 or higher and the following libraries installed:

- Pygame
- NEAT-Python

You can install the required libraries using the following command:
pip install pygame neat-python


## Project Structure

The project consists of the following files:

- `main.py`: The main Python script that contains the game logic and the NEAT implementation.
- `dino.png`: Image of the dino character.
- `ground.png`: Image of the ground in the game.
- `cactus.png`: Image of the cactus obstacle.
- `config_neat.ini`: Configuration file for the NEAT algorithm.

## Running the Project

To run the project, simply execute the `main.py` script:
python main.py


The game will start, and the AI agent will learn to play the game by evolving its neural network through generations. The training progress will be displayed in the terminal.

Once the training is complete, the winner genome will be saved as `winner_genome.pkl`.
