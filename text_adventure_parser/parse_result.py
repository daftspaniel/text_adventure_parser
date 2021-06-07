""" Result of a Parsing operation """


class ParseResult:
    """Result class to be used by apps to action operations."""

    def __init__(self):
        self.understood = False
        self.verb = ""
        self.noun = ""

    def __str__(self) -> str:
        return (
            str(self.understood)
            + "\t"
            + self.verb
            + "\t"
            + (self.noun if self.noun is not None else "")
        )

    def dummy(self):
        """dummy method"""
        print("Hey!" + self.verb)
