# game/game_manager.py

import pygame


class GameManager:
    # Class-level attribute to hold the singleton instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Implementing the Singleton pattern, Ensuring only one instance is created
        if cls._instance is None:
            cls._instance = super(GameManger, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Only initialize if it hasn't been done before
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.current_bank_level = 1  # Starting at "Small Town Bank:
            self.screen - None  # Place holder for the game screen
            self.running = True  # Control the game loop

    def start_game(self, screen):
        # Store the game screen for rendering
        self.screen = screen
        print("Game started at bank level: {self.current_bank_level}")

    def run(self):
        # Main game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen
            self.screen.fill((255, 255, 255))
            # Reder the game elements here (e.g., current bank)

            pygame.display.update()

    def quit(self):
        # Method ot quite the game
        pygame.quit()
        self.running = False
