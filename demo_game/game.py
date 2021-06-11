""" DEMO text adventure game """
from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult

from demo_game.player import Player
from demo_game.room import Room

verbs = ["exit", "go", "get", "put", "inventory", "look"]

nouns = ["gold", "north", "south", "east", "west"]

shorthands = {
    "i": "inventory",
    "n": "go north",
    "s": "go south",
    "e": "go east",
    "w": "go west",
}


class Game:
    """Demo game object"""

    def __init__(self):
        self.parser = Parser(verbs, nouns, shorthands)
        self.player = Player()
        self.arena = [
            [Room("You are in a small wooden hut.", ["N"], ["gold"])]]

    @property
    def current_room(self) -> Room:
        """Returns the current room the player is in."""
        return self.arena[0][0]

    def handle_user_command(self, command: str):
        """Parse the user command and action it."""
        result: ParseResult = self.parser.parse(command)
        print(result)


def main():
    """The game loop"""
    print("Welcome to the game brave adventurer!")
    game = Game()

    while True:
        print('*'*50)
        print()
        print(game.current_room.description)
        print()

        items = game.current_room.items
        if len(items) > 0:
            print('Items : ')
            for item in items:
                print(item)
            print('\n')

        exits = game.current_room.exits
        if len(exits) > 0:
            print('Exits : ')
            for exit in exits:
                print(exit)
            print('\n')

        command = input("\nWhat now?\n")
        game.handle_user_command(command)
