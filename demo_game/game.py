""" DEMO text adventure game """
from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult

from demo_game.player import Player
from demo_game.room import Room
from demo_game.resources import get_vocabulary

verbs, nouns, shorthands = get_vocabulary()


class Game:
    """Demo game object"""

    def __init__(self):
        self.parser = Parser(verbs, nouns, shorthands)
        self.player = Player()
        self.arena = [[]]
        self._build_world()

    def _build_world(self):
        room = Room("You are in a small wooden hut.", ["S"], ["Gold"])
        self.arena[0].append(room)

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
        print("*" * 50)
        print()
        print(game.current_room.description)
        print()

        items = game.current_room.items
        if len(items) > 0:
            print("Items : ")
            for item in items:
                print(item)
            print("\n")

        exits = game.current_room.exits
        if len(exits) > 0:
            print("Exits : ")
            for room_exit in exits:
                print(room_exit)
            print("\n")

        command = input("\nWhat now?\n")
        game.handle_user_command(command)
