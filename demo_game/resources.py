""" Resources and data for demo game"""


def get_vocabulary():
    """Return the vocabulary list for the game."""
    verbs = ["quit", "go", "get", "drop", "look"]

    nouns = [
        "north",
        "south",
        "east",
        "west",
        "n",
        "s",
        "e",
        "w",
        "help",
        "game",
        "inventory",
        "room",
    ]

    nouns.extend(["gold"])

    shorthands = {
        "?": "look help",
        "inventory": "look inventory",
        "help": "look help",
        "look": "look room",
        "quit": "quit game",
        "i": "look inventory",
        "n": "go north",
        "s": "go south",
        "e": "go east",
        "w": "go west",
    }

    return verbs, nouns, shorthands
