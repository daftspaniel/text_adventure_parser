""" DEMO of Toy verb/noun parser for a game or something """

from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult

from demo_game.resources import get_vocabulary

verbs, nouns, shorthands = get_vocabulary()
DIVIDER = "\n" + ("-" * 50) + "\n"

print("\nWelcome to the Parser mini demo.")
print("\tFor a more extensive demo, see run_game.py")
print("\tTo exit type 'quit'.")

command = ""
parser = Parser(verbs, nouns, shorthands)

while command != "quit":
    command = input("\nWhat now?\n")
    result: ParseResult = parser.parse(command)

    print(DIVIDER)
    print(result.explain())
    print(DIVIDER)
