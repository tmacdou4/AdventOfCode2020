

with open("03.in", "r") as file:
    rows = []
    for l in file:
        rows.append(list(l.strip()))

    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    total_count = 1
    for s in slopes:
        tree_count = 0

        curr_row = 0
        curr_col = 0

        while curr_row < len(rows):
            #is_tree?
            if rows[curr_row][curr_col] == '#':
                tree_count += 1

            #advance_pointer
            curr_row += s[1]
            curr_col = (curr_col + s[0]) % len(rows[0])

        total_count = total_count * tree_count

    print(total_count)