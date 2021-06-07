""" Toy verb/noun parser for a game or something """
from text_adventure_parser.parse_result import ParseResult


class Parser:
    """Core Parsing object"""

    def __init__(self, verbs, nouns, shorthands) -> None:
        self.verbs = verbs
        self.nouns = nouns
        self.shorthands = shorthands

    def parse(self, command: str) -> ParseResult:
        """Parse the raw command string from the user."""
        if len(command) == 0:
            return ParseResult()

        command = command.lower()

        is_single_word = command.find(" ") == -1

        if is_single_word and command in self.shorthands.keys():
            command = self.shorthands[command]
            is_single_word = command.find(" ") == -1

        print("COMMAND:", command)

        return (
            self._parse_single_word(command)
            if is_single_word
            else self._parse_multiple_words(command)
        )

    def _parse_single_word(self, command):
        result = ParseResult()
        if command in self.verbs:
            verb = command
            result.verb = verb
            result.noun = None
            result.understood = True
        return result

    def _parse_multiple_words(self, command):
        result = ParseResult()
        words = command.split(" ")

        if words[0] in self.verbs:
            result.verb = words[0]
        if words[1] in self.nouns:
            result.noun = words[1]

        result.understood = True

        return result

    def dummy(self):
        """Dummy method"""
        print(self.verbs)
