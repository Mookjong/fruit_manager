from typing import Dict
import json

def load_inventory(file_path: str) -> Dict[str, int]:
    try:
        with open(file_path, 'r') as file:
            inventory: Dict[str, int] = json.load(file)
            
    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding inventory file. Starting with an empty inventory.")
        return {}
    else:   
        return inventory
    
    
def save_inventory(file_path: str, inventory: Dict[str, int]):
    with open(file_path, 'w') as file:
        json.dump(inventory, file, indent=4)


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
    
    inventory_file = "./data/fruit_inventory.json"
    inventory = load_inventory(inventory_file)

    display_inventory(inventory)
    harvest_fruit(inventory, "banana", 10)
    sell_fruit(inventory, "apple", 4)
    display_inventory(inventory)
    save_inventory(inventory_file, inventory)
