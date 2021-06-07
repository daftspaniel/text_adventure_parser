""" Result of a Parsing operation """


class ParseResult:
    def __init__(self):
        self.understood = False
        self.verb = ''
        self.noun = ''

    def __str__(self) -> str:
        return str(self.understood) \
               + '\t' + self.verb \
               + '\t' + (self.noun if self.noun is not None else '')
