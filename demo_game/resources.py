""" Resources and data for demo game"""


def get_vocabulary():
    """Returnd the vocabulary list for the game."""
    verbs = ["exit", "go", "get", "put", "inventory", "look"]

    nouns = ["gold", "north", "south", "east", "west", "help"]

    shorthands = {
        "?": "look help",
        "help": "look help",
        "i": "look inventory",
        "n": "go north",
        "s": "go south",
        "e": "go east",
        "w": "go west",
    }

    return verbs, nouns, shorthands
