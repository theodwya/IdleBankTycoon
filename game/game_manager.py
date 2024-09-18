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
            self.total_cash = 1000  # Placeholder for player's cash
            self.income_per_second = 50  # Placeholder for player's income per second
            self.current_bank = Bank("Small Town Bank", 1.0)
            self.screen = None  # Place holder for the game screen
            self.running = True  # Control the game loop
            self.current_screen = 'main'

            # Load iconds for the invformation bar
            self.level_icon = pygame.image.load('game/assets/level_icon.png')
            self.cash_icon = pygame.image.load('game/assets/cash_icon.png')
            self.income_icon = pygame.image.load('game/assets/income_icon.png')

    def draw_information_bar(self):
        # Background for the informaion bar
        pygame.draw.rect(self.screen, (30, 30, 30),
                         (0, 0, 800, 50))  # Dark background

        # Set up the font for the text
        font = pygame.font.SysFont(None, 24)

        # Draw the player level with icon
        self.screen.blit(self.level_icon, (20, 10))
        level_text = font.render(
            f"Level: {self.current_bank_level}", True, (255, 255, 255))
        self.screen.blit(level_text, (60, 15))

        # Draw the total cash with icon
        self.screen.blit(self.cash_icon, (200, 10))
        cash_text = font.render(f"${self.total_cash}", True, (255, 255, 255))
        self.screen.blit(cash_text, (440, 15))

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle button clicks
                    self.handle_click(event.pos)

            # Clear the screen
            self.screen.fill((255, 255, 255))
            # Reder the game elements here (e.g., current bank)

            # Draw the information bar
            self.draw_information_bar()

            # Draw the appropriate screen
            if self.current_screen == 'main':
                self.draw_main_screen()
            elif self.current_screen == 'marketing_office':
                self.current_bank.draw_section(
                    self.screen, 'marketing_office')
                # TODO Add other sections here

            pygame.display.update()

    def handle_click(self, pos):
        if self.current_screen == 'main':
            # Handle clicks for room navigation buttons here in the future
            pass
        else:
            # Handle clicks on upgrade buttons within a section
            self.current_bank.handle_click(pos, self.current_screen)

    def quit(self):
        # Method ot quite the game
        pygame.quit()
        self.running = False
