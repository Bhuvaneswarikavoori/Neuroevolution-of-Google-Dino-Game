# Neuroevolution of Dino Game

This project is an implementation of the Google Dino Game using Python, Pygame, and the NEAT (NeuroEvolution of Augmenting Topologies) algorithm. The objective is to train an AI agent to play the game and avoid obstacles by learning to jump over cacti.

In this game, a virtual dinosaur is running through a landscape, encountering various cacti as obstacles. The AI agent learns to control the dinosaur by making well-timed jumps to avoid colliding with the cacti.

## Algorithm and Learning Process

The core of this project lies in the use of the NEAT algorithm, a powerful genetic algorithm that evolves neural networks through a process of mutation, crossover, and selection. The AI agent learns to play the game better with each generation of neural networks.

As the generations evolve, the neural networks develop the ability to make better decisions for jumping over cacti. The learning process involves evaluating each neural network based on its performance in the game, assigning a fitness score, and selecting the best-performing networks to create the next generation.

This approach allows the AI agent to learn from scratch and discover new strategies for playing the game without any explicit guidance or predefined rules.


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
