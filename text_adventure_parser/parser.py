""" Toy verb/noun parser for a game or something """
from typing import List
from text_adventure_parser.parse_result import ParseResult


class Parser:
    """Core Parsing object"""

    def __init__(self, verbs, nouns, shorthands) -> None:
        self.verbs = verbs
        self.nouns = nouns
        self.shorthands = shorthands
        self._result = ParseResult("")

    def get_known_verbs(self) -> List[str]:
        """Return the list of known verbs."""
        return self.verbs.copy()

    def parse(self, command: str) -> ParseResult:
        """Parse the raw command from the user and return ParseResult."""
        self._result = ParseResult(command)
        if len(command) == 0:
            return self._result
        self._preprocess(command)

        return self._parse()

    def _preprocess(self, command):
        short = self.shorthands
        command = command.lower()
        self._result.processed_command = (
            short[command] if command in short.keys() else command
        )

    def _parse(self):
        result = self._result
        words = result.processed_command.split(" ")
        result.verb = words[0]
        result.noun = words[1]
        if words[0] in self.verbs:
            result.understood_verb = True
        if words[1] in self.nouns:
            result.understood_noun = True

        return result
