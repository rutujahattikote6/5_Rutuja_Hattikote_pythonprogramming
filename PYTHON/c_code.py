n = 5

# Loop to print upper triangle
for rows in range(1, n + 1):
    # Print spaces
    for columns in range(n, rows, -1):
        print(" ", end="")

    # Print star
    print("*", end="")

    # Print spaces between stars
    for columns in range(1, (rows - 1) * 2 + 1):
        print(" ", end="")

    # Print star or newline
    if rows == 1:
        print()
    else:
        print("*")

# Loop to print lower triangle
for rows in range(n - 1, 0, -1):
    # Print spaces
    for columns in range(n, rows, -1):
        print(" ", end="")

    # Print star
    print("*", end="")

    # Print spaces between stars
    for columns in range(1, (rows - 1) * 2 + 1):
        print(" ", end="")

    # Print star or newline
    if rows == 1:
        print()
    else:
        print("*")
