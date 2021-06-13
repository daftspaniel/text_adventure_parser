""" DEMO of Toy verb/noun parser for a game or something """

from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult

from demo_game.resources import get_vocabulary

verbs, nouns, shorthands = get_vocabulary()


print("Welcome to the Parser mini demo.")
parser = Parser(verbs, nouns, shorthands)

while True:
    command = input("\nWhat now?\n")

    result: ParseResult = parser.parse(command)

    print("\n" + ("-" * 50) + "\n")
    print(result.explain())
    print("-" * 50)
