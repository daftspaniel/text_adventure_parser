""" Result of a Parsing operation """


class ParseResult:
    """Result class to be used by apps to action operations."""

    def __init__(self):
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
    def understood(self):
        """Overall flag for whether the command was understood."""
        return self.understood_verb and self.understood_noun
