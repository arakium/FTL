
guests = {}

# {"name": (age, email)}

# --- Logic Layer ---

def get_guests() -> dict:
    return guests

def add_guest(name, *args) -> str:
    guests[name] = args
    return name

def remove_guest(name: str) -> str:
    guests.pop(name)
    return name

# --- Presentation Layer (CLI) ---

def show_guests_cli():
    """
    Fetches current guests from guests list and displays it to the user in CLI
    """
    try:
        current = get_guests()
    except Exception: # No use for now.. just to handle errors in case we use files/dbs instead of lists 
        print(f"error: couldn't fetch guests from source.")
        return

    if not current:
        print("There are no guests.")
    else:
        print("=== Current Guests ==")
        for index, (key, value) in enumerate(current.items(), 1):
            print(f"{index}. | Guest name: {key} | Guest age: {value[0]} | Guest email: {value[1]}")


def add_guest_cli():
    """
    Takes guest information from the user and calls add_guest to add a new guest.
    """
    name = input("Enter the guest's name you want to add: ").strip()
    age = input("Enter the guest's age you want to add: ").strip()
    email = input("Enter the guest's email you want to add: ").strip()
    try:
        add_guest(name, age, email)
    except Exception: # No use for now.. just to handle errors in case we use files/dbs instead of lists 
        print(f"error: couldn't add the guest: {name}")
        return
    
    print(f"{name} was added successfully.")

def remove_guest_cli():
    """
    Takes a name frm the user and removes that name from guests
    """
    name = input("Enter the guest's name you want to remove: ").strip()

    try:
        remove_guest(name)
    except KeyError:
        print(f"error: {name} isn't a guest.")
        return

    print(f"\n{name} was removed successfully.")


# CLI Controller
actions = {"1": show_guests_cli,
            "2": add_guest_cli,
            "3": remove_guest_cli
            }

def cli():
    """
    Command Line Interface for interaction with Terminal
    """
    while True:
        print("#"*5 + " Guests Management System " + "#"*5)
        print("Available actions: \n"
            "1. Show current guests\n"
            "2. Add new guest\n"
            "3. Remove current guest"
              )

        choice = input("Enter a number from the list ('q' to quit): ").strip()
        if choice == "q":
            break
        try:
            print("\n")
            actions[choice]()
            print("\n")
        except KeyError:
            print("There is no such action. Please Enter an available action from the list.\n")
            continue

if __name__ == "__main__":
    cli()
