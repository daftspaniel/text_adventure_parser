""" DEMO text adventure game """
from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult
from text_adventure_parser.text_util import list_to_text

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

        if not result.understood:
            print("\nSorry - I don't know how to '" + command + "'")
            return

        if result.processed_command == "quit game":
            exit(0)
        elif result.processed_command == "look help":
            print("\nWords I know :")
            print(list_to_text(self.parser.get_known_verbs()))
        else:
            print("\nI understood the command.\n")
            print("The game has not implemented '" + command + "' yet.\n")


def main():
    """The game loop"""
    game = Game()

    print("*" * 50)
    print("\n\nWelcome to the game brave adventurer!")
    print("Type 'help' or '?' to see what words I understand.")

    while True:
        print(" ")
        print("*" * 50)
        print(" ")
        print(game.current_room.description)
        print("")

        items = game.current_room.items
        exits = game.current_room.exits

        print("Items : " + list_to_text(items))
        print("Exits : " + list_to_text(exits))

        command = input("\nWhat now?\n")
        game.handle_user_command(command)
