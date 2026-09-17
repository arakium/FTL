

while True:
    n = input("Enter the number of rows: ")
    m = input("Enter the number of columns: ")
    if not n.isdigit() or not m.isdigit():
        print("Please enter valid integers for rows and columns.")
        continue

    n = int(n)
    m = int(m)
    if n <= 0 or m <= 0:
        print("Please enter positive integers for rows and columns.")
        continue

    treasure_x = input(f"choose a row to hide the treasure: 1-{n}: ")
    treasure_y = input(f"choose a column to hide the treasure: 1-{m}: ")
    if not treasure_x.isdigit() or not treasure_y.isdigit():
        print("Please enter valid integers for treasure coordinates.")
        continue

    treasure_x = int(treasure_x)
    treasure_y = int(treasure_y)
    if treasure_x < 1 or treasure_x > n or treasure_y < 1 or treasure_y > m:
        print(f"Please enter valid coordinates within the range: 1-{n} for rows and 1-{m} for columns.")
        continue

    board = [["*" for _ in range(m)] for _ in range(n)]
    board[treasure_x - 1][treasure_y - 1] = "T"

    place_trap = input("Do you want to place a trap? (yes/no): ").strip().lower()
    trap_x = trap_y = None
    if place_trap == "yes":
        trap_x = input(f"choose a row to place the trap: 1-{n}: ")
        trap_y = input(f"choose a column to place the trap: 1-{m}: ")
        if not trap_x.isdigit() or not trap_y.isdigit():
            print("Please enter valid integers for trap coordinates.")
            continue

        trap_x = int(trap_x)
        trap_y = int(trap_y)
        if trap_x < 1 or trap_x > n or trap_y < 1 or trap_y > m:
            print(f"Please enter valid coordinates within the range: 1-{n} for rows and 1-{m} for columns.")
            continue
        board[trap_x - 1][trap_y - 1] = "X"

    print("Here's your board:")
    for row in board:
        print(" ".join(row))



    while True:
        guess_x = input(f"Guess the row (1-{n}): ")
        guess_y = input(f"Guess the column (1-{m}): ")
        if not guess_x.isdigit() or not guess_y.isdigit():
            print("Please enter valid integers for your guess.")
            continue

        guess_x = int(guess_x)
        guess_y = int(guess_y)
        if guess_x < 1 or guess_x > n or guess_y < 1 or guess_y > m:
            print(f"Please enter valid coordinates within the range: 1-{n} for rows and 1-{m} for columns.")
            continue

        if guess_x == treasure_x and guess_y == treasure_y:
            print("Congratulations! You found the treasure!")
            board[guess_x - 1][guess_y - 1] = "T"
            break
        else:
            print("Sorry, that's not the correct location. Try again.")
            board[guess_x - 1][guess_y - 1] = "X"
    break
