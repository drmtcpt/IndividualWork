import json
import time

items = []
MENU_OPTIONS = {
    "1": "Add New Item",
    "2": "View All Items",
    "3": "Search Item",
    "4": "Update Item",
    "5": "Delete Item",
    "6": "Calculate Summary Stats",
    "7": "Save to File",
    "8": "Load from File",
    "9": "Sort Items by Field",
    "10": "Recursive Count",
    "11": "Help / Instructions",
    "12": "Clear All Data",
    "0": "Exit"
}

def welcome_screen():
    ascii_art = r"""
    *****************************************
    *      WELCOME TO INVENTORY SYSTEM      *
    *   A Simple Inventory Management App   *
    *       Developed by Ali Najali         *
    *             Version 1.0               *
    *****************************************
    """
    print(ascii_art)
    time.sleep(2)

def main_menu():
    print("\n======= MAIN MENU =======")
    for key, value in MENU_OPTIONS.items():
        print(f"{key}. {value}")
    print("=========================")

def input_item():
    try:
        item = {
            "id": input("Enter Item ID: ").strip(),
            "name": input("Enter Item Name: ").strip(),
            "quantity": int(input("Enter Item Quantity: ").strip())
        }
        items.append(item)
        print("✅ Item added successfully.")
    except ValueError:
        print("❌ Invalid input! Quantity must be a number.")

def view_items():
    if not items:
        print("⚠️ No records available.")
    else:
        print("{:<10}{:<20}{:<10}".format("ID", "Name", "Quantity"))
        print("-" * 40)
        for i in items:
            print("{:<10}{:<20}{:<10}".format(i["id"], i["name"], i["quantity"]))

def search_item():
    iid = input("Enter Item ID to search: ").strip()
    for i in items:
        if i["id"] == iid:
            print("✅ Found:", i)
            return
    print("❌ Item not found.")

def update_item():
    iid = input("Enter Item ID to update: ").strip()
    for i in items:
        if i["id"] == iid:
            i["name"] = input("Enter New Name: ").strip()
            try:
                i["quantity"] = int(input("Enter New Quantity: ").strip())
            except ValueError:
                print("❌ Invalid quantity. Skipped.")
            print("✅ Item updated successfully.")
            return
    print("❌ Item not found.")

def delete_item():
    iid = input("Enter Item ID to delete: ").strip()
    for idx, i in enumerate(items):
        if i["id"] == iid:
            del items[idx]
            print("✅ Item deleted successfully.")
            return
    print("❌ Item not found.")

def summary_stats():
    if not items:
        print("⚠️ No records to summarize.")
        return
    total = sum(i["quantity"] for i in items)
    avg = total / len(items)
    print(f"📊 Total Items: {len(items)}")
    print(f"📊 Average Quantity: {avg:.2f}")

def save_to_file():
    with open("inventory.json", "w") as f:
        json.dump(items, f)
    print("✅ Data saved to 'inventory.json'.")

def load_from_file():
    global items
    try:
        with open("inventory.json", "r") as f:
            items = json.load(f)
        print("✅ Data loaded from 'inventory.json'.")
    except FileNotFoundError:
        print("❌ No file found.")
    except json.JSONDecodeError:
        print("❌ File is corrupted.")

def sort_items():
    key = input("Sort by 'id', 'name', or 'quantity': ").strip()
    if key in ["id", "name", "quantity"]:
        items.sort(key=lambda x: x[key])
        print(f"✅ Items sorted by {key}.")
    else:
        print("❌ Invalid field.")

def recursive_count(index=0):
    if index >= len(items):
        return 0
    return 1 + recursive_count(index + 1)

def help_menu():
    print("""
    📖 Instructions:
    - Use the menu numbers to choose an operation.
    - Ensure item IDs are unique.
    - Use 'Save to File' before exiting to keep your data.
    - Use 'Load from File' to retrieve saved records.
    """)

def clear_data():    
    confirm = input("⚠️ Are you sure you want to delete all data? (yes/no): ").strip().lower()
    if confirm == "yes":
        items.clear()
        print("✅ All data cleared.")
    else:
        print("❌ Operation cancelled.")

def main():
    welcome_screen()
    while True:
        main_menu()
        choice = input("Choose an option: ").strip()
        try:
            match choice:
                case "1": input_item()
                case "2": view_items()
                case "3": search_item()
                case "4": update_item()
                case "5": delete_item()
                case "6": summary_stats()
                case "7": save_to_file()
                case "8": load_from_file()
                case "9": sort_items()
                case "10": print(f"Total records (recursively): {recursive_count()}")
                case "11": help_menu()
                case "12": clear_data()
                case "0":
                    print("👋 Goodbye!")
                    break
                case _: print("❌ Invalid choice. Please try again.")
        except Exception as e:
            print("❌ An error occurred:", str(e))

if __name__ == "__main__":
    main()
