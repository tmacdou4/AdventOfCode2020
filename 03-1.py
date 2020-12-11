
with open("03.in", "r") as file:
    rows = []
    for l in file:
        rows.append(list(l.strip()))

    tree_count = 0

    curr_row = 0
    curr_col = 0

    while curr_row < len(rows):
        #is_tree?
        if rows[curr_row][curr_col] == '#':
            tree_count += 1

        #advance_pointer
        curr_row += 1
        curr_col = (curr_col + 3) % len(rows[0])

    print(tree_count)