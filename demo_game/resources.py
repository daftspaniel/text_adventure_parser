""" Resources and data for demo game"""


def get_vocabulary():
    """Returnd the vocabulary list for the game."""
    verbs = ["quit", "go", "get", "put", "inventory", "look"]

    nouns = ["gold", "north", "south", "east", "west", "help", "game"]

    shorthands = {
        "?": "look help",
        "help": "look help",
        "quit": "quit game",
        "i": "look inventory",
        "n": "go north",
        "s": "go south",
        "e": "go east",
        "w": "go west",
    }

    return verbs, nouns, shorthands
