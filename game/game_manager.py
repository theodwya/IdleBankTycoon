# game/game_manager.py

import pygame
from .bank import Bank


class GameManager:
    # Class-level attribute to hold the singleton instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Implementing the Singleton pattern, Ensuring only one instance is created
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Only initialize if it hasn't been done before
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.current_bank_level = 1  # Starting at "Small Town Bank:
            self.current_bank = Bank("Small Town Bank", 1.0)
            self.screen = None  # Place holder for the game screen
            self.running = True  # Control the game loop

    def start_game(self, screen):
        # Store the game screen for rendering
        self.screen = screen
        print("Game started at bank level: {self.current_bank_level}")
        print(f" Current Bank Income: {self.current_bank.calculate_income()}")

    def run(self):
        # Main game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen
            self.screen.fill((255, 255, 255))
            # Reder the game elements here (e.g., current bank)

            # Display bank info (Temporary for testing)
            font = pygame.font.SysFont(None, 36)
            text = font.render(
                f"Bank: {self.current_bank.name}, Income: {self.current_bank.calculate_income()}", True, (0, 0, 0))
            self.screen.blit(text, (20, 20))

            pygame.display.update()

    def quit(self):
        # Method ot quite the game
        pygame.quit()
        self.running = False
