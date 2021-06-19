"""Adventure game engine object"""
import sys

from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult
from text_adventure_parser.text_util import label_list

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
        room1 = Room("You are in a small wooden hut.", ["s", "e"], ["gold"])
        room3 = Room("You are next to a small pond.", ["w"], [])
        self._arena[0].append(room1)
        self._arena[0].append(room3)
        room2 = Room("You are in a fenced garden.", ["n"], [])
        self._arena[1].append(room2)

    @property
    def current_room(self) -> Room:
        """Returns the current room the player is in."""
        return self._arena[self._player.map_y][self._player.map_x]

    @property
    def response(self) -> str:
        """Returns the response to the player's command."""
        return self._command_response

    @property
    def redisplay_room(self) -> str:
        """Returns the flag for redisplaying the room."""
        return self._redisplay_room

    def handle_user_command(self, command: str):
        """Parse the user command and action it."""
        result: ParseResult = self._parser.parse(command)
        self._redisplay_room = False

        if not result.understood:
            response = "Sorry - I don't know how to '" + command + "'."
        elif result.processed_command == "quit game":
            sys.exit(0)
        elif result.verb == "go":
            response = self._handle_go(result)
        elif result.verb == "get":
            response = self._handle_get(result)
        elif result.verb == "drop":
            response = self._handle_drop(result)
        elif result.verb == "look":
            response = self._handle_look(result)
        else:
            response = (
                "I understood the command.\nHowever '"
                + command
                + "' is not implemented yet."
            )
        self._command_response = response

    def _handle_drop(self, result):
        if result.noun not in self._player.inventory:
            return "You are not carrying a " + result.noun + "."
        self._player.drop_item(result.noun)
        self.current_room.add_item(result.noun)
        return "You drop the " + result.noun + "."

    def _handle_get(self, result):
        if result.noun not in self.current_room.items:
            return "There is no " + result.noun + " here."
        self._player.collect_item(result.noun)
        self.current_room.remove_item(result.noun)
        return "You take the " + result.noun + "."

    def _handle_look(self, result):
        if result.noun == "inventory":
            return label_list("You are carrying", self._player.inventory)
        if result.noun == "help":
            return label_list("Words I know", self._parser.verbs)
        return ""

    def _handle_go(self, result):
        direction = result.noun[0]
        if direction not in self.current_room.exits:
            return "You can't go in that direction."

        self._redisplay_room = True
        if direction == "s":
            self._player.map_y += 1
        elif direction == "n":
            self._player.map_y -= 1
        elif direction == "e":
            self._player.map_x += 1
        elif direction == "w":
            self._player.map_x -= 1

        return ""
