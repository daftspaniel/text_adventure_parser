""" DEMO text adventure game """
import sys

from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult
from text_adventure_parser.text_util import list_to_text

from demo_game.player import Player
from demo_game.room import Room
from demo_game.resources import get_vocabulary

verbs, nouns, shorthands = get_vocabulary()
DIVIDER = "\n" + ("-" * 50) + "\n"


class Game:
    """Demo game object"""

    def __init__(self):
        self.parser = Parser(verbs, nouns, shorthands)
        self.player: Player = Player()
        self.arena = [[], []]
        self._build_world()

    def _build_world(self):
        room1 = Room("You are in a small wooden hut.", ["s"], ["gold"])
        self.arena[0].append(room1)
        room2 = Room("You are in a fenced garden.", ["n"], [])
        self.arena[1].append(room2)

    @property
    def current_room(self) -> Room:
        """Returns the current room the player is in."""
        return self.arena[self.player.map_y][self.player.map_x]

    def handle_user_command(self, command: str):
        """Parse the user command and action it."""
        result: ParseResult = self.parser.parse(command)

        if not result.understood:
            print("\nSorry - I don't know how to '" + command + "'")
            return

        if result.processed_command == "quit game":
            sys.exit(0)
        elif result.verb == "go" and result.noun[0] in self.current_room.exits:
            if result.noun[0] == "s":
                self.player.map_y += 1
            elif result.noun[0] == "n":
                self.player.map_y -= 1
        elif result.verb == "get" and result.noun in self.current_room.items:
            self.player.collect_item(result.noun)
            self.current_room.remove_item(result.noun)
        elif result.verb == "drop" and result.noun in self.player.inventory:
            self.player.drop_item(result.noun)
            self.current_room.add_item(result.noun)
        elif result.processed_command == "look inventory":
            print("\nYou are carrying :")
            print(list_to_text(self.player.inventory))
        elif result.processed_command == "look help":
            print("\nWords I know :")
            print(list_to_text(self.parser.get_known_verbs()))
        else:
            print("\nI understood the command.\n")
            print("However '" + command + "' is not implemented yet.\n")


def main():
    """The game loop"""
    game = Game()

    print(DIVIDER)
    print("Welcome to the game brave adventurer!")
    print("Type 'help' or '?' to see what words I understand.")

    while True:
        print(DIVIDER)
        print(game.current_room.description)
        print("")

        items = game.current_room.items
        exits = game.current_room.exits

        print("Items : " + list_to_text(items))
        print("Exits : " + list_to_text(exits))

        command = input("\nWhat now?\n")
        game.handle_user_command(command)
