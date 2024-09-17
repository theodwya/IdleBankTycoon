# game/ui.py

import pygame


class UpgradeButton:
    def __init__(self, item, x, y, width, height,):
        self.item = item  # Reference to the upgradable item
        # Define button size and position
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, 24)  # Font for rendering text
        self.color = (100, 200, 100)  # Default button color (green)

    def draw(self, screen):
        # Draw the button rectangle
        pygame.draw.rect(screen, self.color, self.rect)
        # Render the items's name, level, and upgrade cost
        text = self.font.render(
            f"{self.item.name} (Lvl: {self.item.level}) - Cost: ${self.item.upgrade_cost}", True, (0, 0, 0))
        # Draw the text on the button
        screen.blit(text, (self.rect.x + 5, self.rect.y + 5))

    def is_clicked(self, pos):
        # Check if the button was clicked based on mouse position
        return self.rect.collidepoint(pos)

    def upgrade(self):
        # Upgrade the item when the button is clicked
        self.item.upgrade()
