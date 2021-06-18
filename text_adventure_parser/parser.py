""" Toy verb/noun parser for a game or something """
from typing import List
from text_adventure_parser.parse_result import ParseResult


class Parser:
    """Core Parsing object"""

    def __init__(self, verbs, nouns, shorthands) -> None:
        self._verbs = verbs
        self._nouns = nouns
        self._shorthands = shorthands
        self._result = ParseResult("")

    @property
    def verbs(self) -> List[str]:
        """Return a copy the list of known verbs."""
        return self._verbs.copy()

    def parse(self, command: str) -> ParseResult:
        """Parse the raw command from the user and return ParseResult."""
        self._result = ParseResult(command)
        if len(command) > 0 and self._preprocess(command):
            return self._parse()
        return self._result

    def _preprocess(self, command):
        short = self._shorthands
        command = command.lower()
        self._result.processed_command = (
            short[command] if command in short.keys() else command
        )
        return self._result.processed_command.find(" ") > -1

    def _parse(self):
        result = self._result
        words = result.processed_command.split(" ")
        result.verb = words[0]
        result.noun = words[1]
        if words[0] in self._verbs:
            result.understood_verb = True
        if words[1] in self._nouns:
            result.understood_noun = True

        return result
