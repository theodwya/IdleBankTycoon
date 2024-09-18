# game/bank.py

from .upgrade import Upgradeable
from .ui import UpgradeButton


class Bank:
    def __init__(self, name, income_multiplier):
        self.name = name  # Name of the bank (e.g., "Small Town Bank")
        # Multiplier for income at this level
        self.income_multiplier = income_multiplier
        self.marketing_office = self.create_marketing_office()
        self.main_hall = self.create_main_hall()
        self.service_area = self.create_service_area()
        self.valut_room = self.create_valut_room()

        # List to store upgrade buttons
        self.upgrade_buttons = {
            "marketing_office": [],
            "main_hall": [],
            "service_area": [],
            "valut_room": []
        }
        self.create_upgrade_buttons()

    def create_marketing_office(self):
        # Create a list of upgradable items in the marketing office
        return [
            Upgradeable("Marketing Desk", 900, 100),
            Upgradeable("Marketing Office Decorations", 850, 50),
            Upgradeable("Rest Area", 950, 150),
            Upgradeable("Lounge", 800, 200),
            Upgradeable("Meeting Room", 850, 150)
        ]

    def create_main_hall(self):
        # Create a list of upgradable items in the main hall
        return [
            Upgradeable("Recerptions Desk", 850, 200),
            Upgradeable("Cafe", 750, 100),
            Upgradeable("Lounge", 650, 250),
            Upgradeable("Fountains", 900, 250),
            Upgradeable("Waiting Area", 900, 200)
        ]

    def create_service_area(self):
        # Create a list of upgradable items in the service area
        return [
            Upgradeable("Service Teller Desk", 950, 150),
            Upgradeable("Service Area Electronics", 850, 100),
            Upgradeable("Break Room", 800, 150),
            Upgradeable("Stock Price Monitor", 900, 200)
        ]

    def create_valut_room(self):
        # Create a list of upgradable items in the vault room
        return [
            Upgradeable("Vault", 950, 450),
            Upgradeable("Vault Security System", 900, 200),
            Upgradeable("Transporter", 850, 425),
            Upgradeable("Statue", 800, 275),
            Upgradeable("Locker Room", 950, 185)
        ]

    def create_upgrade_buttons(self):
        # Create buttons for all upgradable items in the bank
        for section, items in zip(['marketing_office', 'main_hall', 'service_area', 'valult_room'],
                                  [self.marketing_office, self.main_hall, self.service_area, self.valut_room]):
            y_offset = 100
            for item in items:
                button = UpgradeButton(item, 20, y_offset, 400, 50)
                self.upgrade_buttons[section].append(button)
                y_offset += 60

    def draw_section(self, screen, section):
        # Draw all upgrade buttons on the screen
        for button in self.upgrade_buttons[section]:
            button.draw(screen)

    def handle_click(self, pos, section):
        # Check if any button was clicked and perform the upgrade
        for button in self.upgrade_buttons:
            if button.is_clicked(pos):
                button.upgrade()
