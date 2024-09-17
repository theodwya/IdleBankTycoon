# game/upgrade.py

class Upgradeable:
    def __init__(self, name, max_level, base_cost):
        self.name = name  # Name of the upgradable item
        self.level = 1  # Initial level
        self.max_level = max_level  # Maximum level this item can reach
        self.base_cost = base_cost  # Initial cost to upgrade
        self.upgrade_cost = base_cost  # Current upgrade cost

    def upgrade(self):
        if self.level < self.max_level:
            self.level += 1
            self.upgrade_cost = int(
                self.base_cost * (1.01 ** self.level))  # Increase the cost by 1%
            print(
                f"{self.name} upgraded to level {self.level}. Next upgrade cost: {self.upgrade_cost}")
        else:
            print(f"{self.name} is already at maximum level!")

    def get_income_boost(self):
        # Return income boost based on the current level
        return self.level * 0.050  # Example: Each level provides a 5% boost in income
