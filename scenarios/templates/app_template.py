# scenarios/templates/app_template.py


def parse_and_sum_inventory(inventory_lines):
    """Parses a list of inventory strings formatted as 'ITEM_NAME:QUANTITY'.

    Example input: ["apples:10", "bananas: 5", "apples: 5", "  oranges: 2  "]

    TODO: Fix the bug where whitespace around item names isn't properly stripped,
    causing duplicate keys ("apples" vs " apples") instead of combining them,
    and handle cases where quantities might be negative or malformed.
    """
    inventory = {}
    for line in inventory_lines:
        if not line or ":" not in line:
            continue

        # Split name and quantity
        parts = line.split(":")
        item_name = parts[0]
        quantity = int(parts[1])

        # Accumulate quantities
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity

    return inventory
