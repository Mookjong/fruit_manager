from typing import Dict
import json
import sys


def load_inventory(file_path: str) -> Dict[str, int]:
    try:
        with open(file_path, "r") as file:
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
    with open(file_path, "w") as file:
        json.dump(inventory, file, indent=4)


def load_treasury(file_path: str) -> float:
    try:
        with open(file_path, "r") as file:
            treasury: float = float(file.read())
    except FileNotFoundError:
        raise FileNotFoundError("Treasury file not found.")
    else:
        return treasury


def save_treasury(file_path: str, treasury: float):
    with open(file_path, "w") as file:
        file.write(f"{treasury:.2f}")
        
        
def display_treasury(treasury: float):
    print(f"Treasury Balance: ${treasury:.2f}")
    print_separator()


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


def sell_fruit(inventory: Dict[str, int], fruit: str, quantity: int, treasury: float = 0.0) -> float | None:
    if fruit in inventory and inventory[fruit] >= quantity:
        inventory[fruit] -= quantity
        treasury += quantity * 2.0  # Assume each fruit sells for $2.0
        print(f"Sold {quantity} units of {fruit}.")
        print_separator()
        return treasury
    else:
        print(f"Not enough {fruit} in inventory to sell.")
    print_separator()
    return None


if __name__ == "__main__":

    inventory_file = "./data/fruit_inventory.json"
    inventory = load_inventory(inventory_file)
    
    treasury_file = "./data/treasuy.txt"
    try:
        treasury = load_treasury(treasury_file)
    except FileNotFoundError:
        print("Treasury file not found. The program will exit.")
        sys.exit("Exiting due to missing treasury file.")
    else:
        display_treasury(treasury)

    display_inventory(inventory)
    harvest_fruit(inventory, "banana", 10)
    
    treasury = sell_fruit(inventory, "apple", 4, treasury) or treasury
    save_treasury(treasury_file, treasury)
    display_treasury(treasury)
    
    display_inventory(inventory)
    save_inventory(inventory_file, inventory)
    
    
