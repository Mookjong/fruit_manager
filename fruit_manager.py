from typing import Dict, List
import json
import sys


def load_inventory(file_path: str) -> Dict[str, int]:
    try:
        with open(file_path, "r") as file:
            inventory: Dict[str, int] = json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError("Inventory file not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Error decoding inventory file.")
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
        
        
def load_price(file_path: str) -> Dict[str, float]:
    try:
        with open(file_path, "r") as file:
            price: Dict[str, float] = json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError("Price file not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Error decoding price file.")
    else:
        return price
    
def load_treasury_history(file_path: str) -> List:
    try:
        with open(file_path, "r") as file:
            history: List = json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError("Treasury history file not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Error decoding treasury history file.")
    else:
        return history
    
def save_treasury_history(file_path: str, history: List):
    with open(file_path, "w") as file:
        json.dump(history, file, indent=4)
        
        
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


def sell_fruit(inventory: Dict[str, int], fruit: str, quantity: int, treasury: float = 0.0, treasury_history: List = None) -> float | None:
    if fruit in inventory and inventory[fruit] >= quantity:
        inventory[fruit] -= quantity
        pricies = load_price("./data/price.json")
        treasury += quantity * pricies.get(fruit, 0)
        treasury_history = treasury_history if treasury_history is not None else []
        treasury_history.append(treasury)
        save_treasury_history("./data/treasury_history.json", treasury_history)
        print(f"Sold {quantity} units of {fruit}.")
        print_separator()
        return treasury
    else:
        print(f"Not enough {fruit} in inventory to sell.")
    print_separator()
    return None


if __name__ == "__main__":

    inventory_file = "./data/fruit_inventory.json"
    try:
        inventory = load_inventory(inventory_file)
    except FileNotFoundError:
        sys.exit("Exiting due to missing inventory file.")
    
    treasury_file = "./data/treasury.txt"
    try:
        treasury = load_treasury(treasury_file)
    except FileNotFoundError:
        sys.exit("Exiting due to missing treasury file.")
    else:
        display_treasury(treasury)
        
    treasury_history_file = "./data/treasury_history.json"
    try:
        treasury_history = load_treasury_history(treasury_history_file)
    except FileNotFoundError:
        sys.exit("Exiting due to missing treasury history file.")
    

    display_inventory(inventory)
    harvest_fruit(inventory, "banana", 10)
    
    treasury = sell_fruit(inventory, "cranberry", 10, treasury, treasury_history)
    save_treasury(treasury_file, treasury)
    display_treasury(treasury)
    
    display_inventory(inventory)
    save_inventory(inventory_file, inventory)
    
    
