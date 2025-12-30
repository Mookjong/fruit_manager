from typing import Dict

inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 15,
    "mango": 12,
    "cranberry": 7,
}


def print_separator():
    print("-" * 30, end="\n")


def display_inventory(inventory):
    print("Current Inventory:")
    for fruit, quantity in inventory.items():
        print(f"{fruit}: {quantity} units")
    print_separator()


def harvest_fruit(inventory: Dict[str, int], fruit: str, quantity: int):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    print(f"Harvested {quantity} units of {fruit}.")
    print_separator()


def sell_fruit(inventory: Dict[str, int], fruit: str, quantity: int):
    if fruit in inventory and inventory[fruit] >= quantity:
        inventory[fruit] -= quantity
        print(f"Sold {quantity} units of {fruit}.")
    else:
        print(f"Not enough {fruit} in inventory to sell.")
    print_separator()


if __name__ == "__main__":

    display_inventory(inventory)
    harvest_fruit(inventory, "banana", 10)
    sell_fruit(inventory, "apple", 4)
    display_inventory(inventory)
