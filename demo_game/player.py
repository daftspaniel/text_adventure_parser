""" Adventure game player module."""


class Player:
    """Demo game player object"""

    def __init__(self):
        self._inventory = []
        self.map_x = 0
        self.map_y = 0

    def __str__(self):
        return str(self._inventory)

    @property
    def inventory(self):
        """Returns a copy of the player's list of items."""
        return self._inventory.copy()

    def collect_item(self, item):
        """Adds an item to the player's inventory."""
        self._inventory.append(item)

    def drop_item(self, item):
        """Adds an item to the player's inventory."""
        self._inventory.remove(item)
