""" DEMO text adventure game """

from text_adventure_parser.text_util import list_to_text
from demo_game.engine import Engine

DIVIDER = "\n" + ("-" * 50) + "\n"


def main():
    """The game loop"""
    game = Engine()

    print(DIVIDER)
    print("Welcome to the game brave adventurer!")
    print("Type 'help' or '?' to see what words I understand.")

    while True:
        print(DIVIDER)
        print(game.current_room.description)
        print("")
        print("Items : " + list_to_text(game.current_room.items))
        print("Exits : " + list_to_text(game.current_room.exits))

        command = input("\nWhat now?\n")
        game.handle_user_command(command)
