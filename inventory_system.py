"""Inventory Management System

Provides basic functions to manage stock items:
add, remove, save, load, and display inventory.
Includes input validation, proper exception handling,
and secure coding practices.
"""

import json


def add_item(stock_data, item, qty, logs=None):
    """Add a specified quantity of an item to the inventory."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str):
        raise TypeError("Item name must be a string.")
    if not isinstance(qty, (int, float)):
        raise TypeError("Quantity must be a number.")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"Added {qty} of {item}")
    return logs


def remove_item(stock_data, item):
    """Remove an item from the inventory if it exists."""
    try:
        del stock_data[item]
        print(f"Removed '{item}' from inventory.")
    except KeyError:
        print(f"Item '{item}' not found in inventory.")


def get_qty(stock_data, item):
    """Return the quantity of a specific item in the inventory."""
    return stock_data.get(item, 0)


def load_data(filename="inventory.json"):
    """Load inventory data from a JSON file and return it."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
            print("Data loaded successfully.")
            return stock_data
    except FileNotFoundError:
        print("No existing data file found. Starting fresh.")
        return {}
    except json.JSONDecodeError:
        print("Error reading JSON file. Starting with empty inventory.")
        return {}


def save_data(stock_data, filename="inventory.json"):
    """Save current inventory data to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
            print("Data saved successfully.")
    except OSError as e:
        print(f"Error saving data: {e}")


def print_data(stock_data):
    """Print all inventory items and quantities."""
    if not stock_data:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item, qty in stock_data.items():
        print(f"- {item}: {qty}")


def check_low_items(stock_data, threshold=5):
    """Print items with quantities below the given threshold."""
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    if not low_items:
        print("No low-stock items.")
    else:
        print("Low-stock items:")
        for item in low_items:
            print(f"- {item}")


def main():
    """Main program to demonstrate inventory system functionality."""
    stock_data = load_data()

    # Example usage with valid input
    logs = add_item(stock_data, "Apples", 10)
    add_item(stock_data, "Bananas", 5, logs)
    print_data(stock_data)

    # Demonstrating safe error handling
    remove_item(stock_data, "Oranges")

    # Check low-stock items
    check_low_items(stock_data, threshold=8)

    # Save data at the end
    save_data(stock_data)

    # Example of invalid input (will raise TypeError)
    # Uncomment below line to test:
    # add_item(stock_data, 123, "ten")

    print("Program completed successfully.")


if __name__ == "__main__":
    main()
