class Room:
    """ Demo game room object"""
    def __init__(self, description, exits, items):
        self.description = description
        self.exits = exits
        self.items = items
