""" Adventure game player module."""


class Player:
    """Demo game player object"""

    def __init__(self):
        self._inventory = []

    def __str__(self):
        return str(self._inventory)

    @property
    def inventory(self):
        """Returns a copy of the player's list of items."""
        return self._inventory.copy()
