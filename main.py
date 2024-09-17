# main.py
import pygame
from game.game_manager import GameManager


def main():
    # Initialize Pygame
    pygame.init()

    # Setup the game screen
    screen = pygame.display.set_mode((800, 600))  # Screen size 800x600 pixels
    pygame.display.set_caption('Idle Bank Tycoon')  # Set the game window title

    # initialize the game manager (Singleton)
    game_manager = GameManager()
    game_manager.start_game(screen)  # Pass the game screen to the game manager

    # Run the game
    game_manager.run()

    # Quit the game
    game_manager.quit()


    # Entry point of the game
if __name__ == '__main__':
    main()
