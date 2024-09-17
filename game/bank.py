# game/bank.py

from .upgrade import Upgradeable


class Bank:
    def __init__(self, name, income_multiplier):
        self.name = name  # Name of the bank (e.g., "Small Town Bank")
        # Multiplier for income at this level
        self.income_multiplier = income_multiplier
        self.marketing_office = self.create_marketing_office()
        self.main_hall = self.create_main_hall()
        self.service_area = self.create_service_area()
        self.valut_room = self.create_valut_room()

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

    def calculate_income(self):
        # Calculate income based on upgrades in all areas
        income = 0
        for area in [self.marketing_office, self.main_hall, self.service_area, self.valut_room]:
            for item in area:
                income += item.get_income_boost()
        return income * self.income_multiplier
