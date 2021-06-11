""" DEMO of Toy verb/noun parser for a game or something """

from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult

verbs = ["exit", "go", "get", "put", "look"]
nouns = ["inventory", "gold", "north", "south", "east", "west"]
shorthands = {
    "i": "look inventory",
    "n": "go north",
    "s": "go south",
    "e": "go east",
    "w": "go west",
}

print("Welcome to the Parser mini demo.")
parser = Parser(verbs, nouns, shorthands)

while True:
    command = input("\nWhat now?\n")

    result: ParseResult = parser.parse(command)

    print("\n" + ("-" * 50) + "\n")
    print(result.explain())
    print("-" * 50)
