"""Handy text functions"""


def yes_no(flag):
    """Boolean to natural readable string."""
    return "Yes" if flag else "No"


def list_to_text(items):
    """Displays a natural list of items."""
    count = len(items)
    items.sort()
    items = [item.capitalize() for item in items]
    result = ""
    if count == 0:
        result = "Nothing"
    elif count == 1:
        result = items[0]
    elif count > 1:
        final_item = items[-1]
        for item in items[:-1]:
            result += item + ", "
        result = result[:-2] + " and " + final_item
    return result + "."
