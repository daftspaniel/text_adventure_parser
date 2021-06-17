"""Handy text functions"""
from typing import List


def yes_no(flag: bool):
    """Boolean to natural readable string."""
    return "Yes" if flag else "No"


def list_to_text(items: List):
    """Displays a natural list of items."""
    count = len(items)
    result = ""
    if count == 0:
        result = "Nothing"
    elif count == 1:
        result = items[0]
    elif count > 1:
        items.sort()
        final_item = items[-1]
        for item in items[:-1]:
            result += item + ", "
        result = result[:-2] + " and " + final_item
    return result.capitalize() + "."


def label_list(label: str, word_list: List):
    """Return a labelled list."""
    return label + ": " + list_to_text(word_list)
