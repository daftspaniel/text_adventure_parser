""" Result of a Parsing operation """
from text_adventure_parser.text_util import yes_no


class ParseResult:
    """Result class to be used by apps to action operations."""

    def __init__(self, command: str):
        self._command = command
        self.processed_command = command
        self.verb = ""
        self.noun = ""
        self.understood_verb = False
        self.understood_noun = False

    def __str__(self) -> str:
        return (
            str(self.understood)
            + "\t"
            + self.verb
            + "\t"
            + (self.noun if self.noun is not None else "")
        )

    @property
    def understood(self) -> bool:
        """Overall flag for whether the command was understood."""
        return self.understood_verb and self.understood_noun

    def explain(self) -> str:
        """Plain text explanation of the parsing result."""
        result = "Parser input was  : " + self._command + "\n"
        result += "After preprocessed was  : " + self.processed_command + "\n"
        result += "Command understood  : " + yes_no(self.understood) + "\n"
        result += "Verb understood  : " + yes_no(self.understood_verb) + "\n"
        result += "Noun understood  : " + yes_no(self.understood_noun) + "\n"
        return result
