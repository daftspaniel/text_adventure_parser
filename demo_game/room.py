""" Adventure game location module."""


class Room:
    """Demo game room object."""

    def __init__(self, description, exits, items):
        self._description = description
        self._exits = exits
        self._items = items

    def __str__(self):
        return self.description + " " + str(self.exits) + str(self.items)

    @property
    def description(self):
        """Current description of the room."""
        return self._description

    @property
    def exits(self):
        """Current exits of the room."""
        return self._exits

    @property
    def items(self):
        """Current items in the room."""
        return self._items

    def remove_item(self, item):
        """Remove an item from the room."""
        self._items.remove(item)

    def add_item(self, item):
        """Add an item to the room."""
        self._items.append(item)
