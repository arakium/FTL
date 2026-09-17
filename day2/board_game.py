import random

# --- Helper functions for input validation ---

def is_digit(*args) -> bool:
    """Check if all provided arguments are strings of digits."""
    for arg in args:
        if not arg.isdigit():
            return False
    return True
    
def is_positive(*args: tuple[int]) -> bool:
    """Check if all provided integer arguments are positive (> 0)."""
    for arg in args:
        if arg <= 0:
            return False
    return True

def contains(x, y, n, m) -> bool:
    """Check if coordinates (x, y) are within the board dimensions (n rows, m columns)."""
    if x < 1 or x > n or y < 1 or y > m:
        return False
    return True

# --- Main game loop ---
while True:
    # Ask player for board size
    n = input("Enter the number of rows: ")
    m = input("Enter the number of columns: ")
    if not is_digit(m, n):
        print("Please enter valid integers for rows and columns.")
        continue

    n = int(n)
    m = int(m)
    if not is_positive(n, m):
        print("Please enter positive integers for rows and columns.")
        continue

    # Ask player where to hide the treasure
    treasure_x = input(f"choose a row to hide the treasure: 1-{n}: ")
    treasure_y = input(f"choose a column to hide the treasure: 1-{m}: ")
    if not is_digit(treasure_x, treasure_y):
        print("Please enter valid integers for treasure coordinates.")
        continue

    treasure_x = int(treasure_x)
    treasure_y = int(treasure_y)
    if not contains(treasure_x, treasure_y, n, m):
        print(f"Please enter valid coordinates within the range: 1-{n} for rows and 1-{m} for columns.")
        continue

    # Create board filled with '*'
    board = [["*" for _ in range(m)] for _ in range(n)]
    # Place treasure visibly (assignment requirement)
    board[treasure_x - 1][treasure_y - 1] = "T"

    # Optional trap placement
    place_trap = input("Do you want to place a trap in a random place? (yes/no): ").strip().lower()
    trap_x = trap_y = None
    if place_trap == "yes":
        while True:
            trap_x = random.randint(1, n)
            trap_y = random.randint(1, m)
            # Ensure trap does not overlap with treasure
            if trap_x != treasure_x or trap_y != treasure_y:
                break

    # --- Guessing loop ---
    while True:
        # Show current board
        print("Here's your board:")
        for row in board:
            print(" ".join(row))
            
        # Ask player for guess
        guess_x = input(f"Guess the row (1-{n}): ")
        guess_y = input(f"Guess the column (1-{m}): ")

        # Validate guess input
        if not is_digit(guess_x, guess_y):
            print("Please enter valid integers for your guess.")
            continue

        guess_x = int(guess_x)
        guess_y = int(guess_y)
        if not contains(guess_x, guess_y, n, m):
            print(f"Please enter valid coordinates within the range: 1-{n} for rows and 1-{m} for columns.")
            continue

        # Check outcomes
        if guess_x == trap_x and guess_y == trap_y:
            print("Oops! You stepped on a trap!")
            print("You lost the game!")
            break

        if guess_x == treasure_x and guess_y == treasure_y:
            print("Congratulations! You found the treasure!")
            board[guess_x - 1][guess_y - 1] = "T"
            break
        else:
            print("Sorry, that's not the correct location. Try again.")
            # Mark wrong guess with 'X'
            board[guess_x - 1][guess_y - 1] = "X"
    break
