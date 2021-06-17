"""Adventure game engine object"""
import sys

from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult
from text_adventure_parser.text_util import list_to_text

from demo_game.player import Player
from demo_game.room import Room
from demo_game.resources import get_vocabulary

verbs, nouns, shorthands = get_vocabulary()


class Engine:
    """Demo game engine object"""

    def __init__(self):
        self._parser: Parser = Parser(verbs, nouns, shorthands)
        self._player: Player = Player()
        self._arena = [[], []]
        self._build_world()
        self._command_response = ""
        self._redisplay_room = True

    def _build_world(self):
        room1 = Room("You are in a small wooden hut.", ["s"], ["gold"])
        self._arena[0].append(room1)
        room2 = Room("You are in a fenced garden.", ["n"], [])
        self._arena[1].append(room2)

    @property
    def current_room(self) -> Room:
        """Returns the current room the player is in."""
        return self._arena[self._player.map_y][self._player.map_x]

    def handle_user_command(self, command: str):
        """Parse the user command and action it."""
        result: ParseResult = self._parser.parse(command)

        if not result.understood:
            print("\nSorry - I don't know how to '" + command + "'")
            return

        if result.processed_command == "quit game":
            sys.exit(0)
        elif result.verb == "go":
            self._handle_go(result)
        elif result.verb == "get" and result.noun in self.current_room.items:
            self._player.collect_item(result.noun)
            self.current_room.remove_item(result.noun)
        elif result.verb == "drop" and result.noun in self._player.inventory:
            self._player.drop_item(result.noun)
            self.current_room.add_item(result.noun)
        elif result.processed_command == "look inventory":
            print("\nYou are carrying :")
            print(list_to_text(self._player.inventory))
        elif result.processed_command == "look help":
            print("\nWords I know :")
            print(list_to_text(self._parser.get_known_verbs()))
        else:
            print("\nI understood the command.\n")
            print("However '" + command + "' is not implemented yet.\n")

    def _handle_go(self, result):
        direction = result.noun[0]
        if direction not in self.current_room.exits:
            print("You can't go in that direction.")
            return

        if direction == "s":
            self._player.map_y += 1
        elif direction == "n":
            self._player.map_y -= 1
