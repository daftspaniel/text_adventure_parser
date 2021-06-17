""" Resources and data for demo game"""


def get_vocabulary():
    """Return the vocabulary list for the game."""
    verbs = ["quit", "go", "get", "drop", "look"]

    nouns = ["north", "south", "east", "west", "help", "game", "inventory"]

    nouns.extend(["gold"])

    shorthands = {
        "?": "look help",
        "inventory": "look inventory",
        "help": "look help",
        "quit": "quit game",
        "i": "look inventory",
        "n": "go north",
        "s": "go south",
        "e": "go east",
        "w": "go west",
    }

    return verbs, nouns, shorthands
