"""
Inventory System - Game Item Management.

Demonstrates:
- Using dictionaries to track item quantities
- Parsing command-line arguments
- Calculating inventory statistics
- Sorting and categorizing items
- Dictionary operations (keys, values, lookup)
"""

import sys


def parse_inventory(args):
    """Parse command-line arguments into an inventory dictionary."""
    inventory = {}
    for arg in args:
        if ":" in arg:
            item, quantity = arg.split(":", 1)
            inventory[item] = int(quantity)
        return inventory


def calculate_total_items(inventory):
    """Calculate the total number of items in the inventory."""
    return sum(inventory.values())


def get_sorted_items(inventory):
    """Return a sorted list of items in the inventory."""
    return sorted(inventory.items(), key=lambda x: (-x[1], x[0]))


def format_unit(quantity):
    """Format the unit string based on quantity."""
    return "unit" if quantity == 1 else "units"


def display_inventory(inventory, total):
    """Display the inventory details."""
    print("=== Current Inventory ===")
    sorted_items = get_sorted_items(inventory)

    for item, quantity in sorted_items:
        percentage = (quantity / total) * 100
        unit_str = format_unit(quantity)
        print(f"{item}: {quantity} {unit_str} ({percentage:.1f}%)")


def get_most_abundant(inventory):
    """Get the item with the highest quantity."""
    if not inventory:
        return None, 0
    return max(inventory.items(), key=lambda x: x[1])


def get_least_abundant(inventory):
    """Get the item with the lowest quantity."""
    if not inventory:
        return None, 0
    return min(inventory.items(), key=lambda x: x[1])


def categorize_items(inventory):
    """Categorize items into abundant and scarce."""
    categories = {
        "Moderate": {},
        "Scarce": {},
    }
    for item, quantity in inventory.items():
        if quantity >= 5:
            categories["Moderate"][item] = quantity
        else:
            categories["Scarce"][item] = quantity
    return categories


def get_restock_items(inventory):
    """Get items that need restocking."""
    restock = [item for item, qty in inventory.items() if qty == 1]
    return sorted(restock)


def main():
    """run the inventory system."""
    if len(sys.argv) < 2:
        print(
            "Usage: python ft_inventory_system.py "
            "item1:quantity1 item2:quantity2 ..."
        )
        return

    # Parse inventory from command-line arguments
    inventory = parse_inventory(sys.argv[1:])

    if not inventory:
        print("No valid inventory items provided.")
        return

    # Calculate totals
    total = calculate_total_items(inventory)
    unique = len(inventory)
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {unique}")

    # Display inventory
    print()
    display_inventory(inventory, total)

    # Statistics
    print()
    print("=== Inventory Statistics ===")
    most_item, most_qty = get_most_abundant(inventory)
    least_item, least_qty = get_least_abundant(inventory)
    print(f"Most abundant: {most_item} ({most_qty} {format_unit(most_qty)})")
    print(f"Least abundant: {least_item} ({least_qty} "
          f"{format_unit(least_qty)})")

    # Categories
    print()
    print("=== Item Categories ===")
    categories = categorize_items(inventory)
    if categories["Moderate"]:
        print(f"Moderate: {categories['Moderate']}")
    if categories["Scarce"]:
        print(f"Scarce: {categories['Scarce']}")

    # management suggestions
    print()
    print("=== Management Suggestions ===")
    restock_items = get_restock_items(inventory)
    print(f"Restock needed: {restock_items}")

    # Dictionary properties demonstration
    print()
    print("=== Dictionary Properties ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


main()
