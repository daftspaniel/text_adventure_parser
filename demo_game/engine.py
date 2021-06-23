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
        self._verb_processor = self._build_verb_processor()

    def _build_verb_processor(self):
        proc = {}
        proc["go"] = self._handle_go
        proc["get"] = self._handle_get
        proc["drop"] = self._handle_drop
        proc["look"] = self._handle_look
        return proc

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
        self._redisplay_room = False
        result: ParseResult = self._parser.parse(command)

        if result.processed_command == "quit game":
            sys.exit(0)

        self._command_response = self._determine_response(command, result)

    def _determine_response(self, command: str, result: ParseResult) -> str:
        if not result.understood_noun:
            response = "There is no " + result.noun + " here."
        elif not result.understood:
            response = "Sorry - I don't know how to '" + command + "'."
        elif result.verb in self._verb_processor:
            response = self._verb_processor[result.verb](result)
        else:
            response = (
                "I understood the command '"
                + result.processed_command
                + "'' but it is not implemented yet."
            )
        return response

    def _handle_drop(self, result: ParseResult) -> str:
        if result.noun not in self._player.inventory:
            return "You are not carrying a " + result.noun + "."
        self._player.drop_item(result.noun)
        self.current_room.add_item(result.noun)
        return "You drop the " + result.noun + "."

    def _handle_get(self, result: ParseResult) -> str:
        if result.noun not in self.current_room.items:
            return "There is no " + result.noun + " here."
        self._player.collect_item(result.noun)
        self.current_room.remove_item(result.noun)
        return "You take the " + result.noun + "."

    def _handle_look(self, result: ParseResult) -> str:
        if result.noun == "room":
            self._redisplay_room = True
            return ""
        if result.noun == "inventory":
            return label_list("You are carrying", self._player.inventory)
        if result.noun == "help":
            return label_list("Words I know", self._parser.verbs)
        if not self._is_item_present(result.noun):
            return "There is no " + result.noun + " here."
        return "Description for " + result.noun

    def _is_item_present(self, noun) -> bool:
        in_room = noun in self.current_room.items
        in_inventory = noun in self._player.inventory
        return in_room or in_inventory

    def _handle_go(self, result: ParseResult) -> str:
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
