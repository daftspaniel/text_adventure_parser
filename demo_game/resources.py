
def get_vocabulary():
    verbs = ["exit", "go", "get", "put", "inventory", "look"]

    nouns = ["gold", "north", "south", "east", "west"]

    shorthands = {
        "i": "look inventory",
        "n": "go north",
        "s": "go south",
        "e": "go east",
        "w": "go west",
    }

    return verbs, nouns, shorthands