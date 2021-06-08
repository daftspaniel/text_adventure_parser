""" Toy verb/noun parser for a game or something """
from typing import List
from text_adventure_parser.parse_result import ParseResult


class Parser:
    """Core Parsing object"""

    def __init__(self, verbs, nouns, shorthands) -> None:
        self.verbs = verbs
        self.nouns = nouns
        self.shorthands = shorthands

    def get_known_verbs(self) -> List[str]:
        """Return the list of known verbs."""
        return self.verbs.copy()

    def parse(self, command: str) -> ParseResult:
        """Parse the raw command string from the user."""
        if len(command) == 0:
            return ParseResult()

        command = self._preprocess(command)

        return self._parse(command)

    def _preprocess(self, command):
        short = self.shorthands
        command = command.lower()
        return short[command] if command in short.keys() else command

    def _parse(self, command):
        result = ParseResult()
        words = command.split(" ")
        result.verb = words[0]
        result.noun = words[1]
        if words[0] in self.verbs:
            result.understood_verb = True
        if words[1] in self.nouns:
            result.understood_noun = True

        return result
