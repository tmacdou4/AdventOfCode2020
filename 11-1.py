import copy

seat_mat = []
with open("11.in", "r") as file:
    for l in file:
        l = list(l.strip())
        seat_mat.append(l)

def check_adj(mat, row, col):
    total_occup = 0

    row_min = True
    col_min = True
    row_max = True
    col_max = True
    if row-1 >= 0:
        row_min = False
    if col-1 >= 0:
        col_min = False
    if row+1 < len(seat_mat):
        row_max = False
    if col+1 < len(seat_mat[0]):
        col_max = False

    #checking positions clockwise from the top left
    if not row_min and not col_min:
        if mat[row-1][col-1] == "#":
            total_occup += 1
    if not row_min:
        if mat[row-1][col] == "#":
            total_occup += 1
    if not row_min and not col_max:
        if mat[row-1][col+1] == "#":
            total_occup += 1
    if not col_min:
        if mat[row][col-1] == "#":
            total_occup += 1
    if not col_max:
        if mat[row][col+1] == "#":
            total_occup += 1
    if not row_max and not col_min:
        if mat[row+1][col-1] == "#":
            total_occup += 1
    if not row_max:
        if mat[row+1][col] == "#":
            total_occup += 1
    if not row_max and not col_max:
        if mat[row+1][col+1] == "#":
            total_occup += 1

    return total_occup

new_mat = copy.deepcopy(seat_mat)

while(True):
    print("iter")
    changed_flag = False
    for i in range(len(new_mat)):
        for j in range(len(new_mat[0])):
            occup = check_adj(seat_mat, i, j)
            if seat_mat[i][j] is "L" and occup == 0:
                new_mat[i][j] = '#'
                changed_flag = True
            elif seat_mat[i][j] is "#" and occup > 3:
                new_mat[i][j] = "L"
                changed_flag = True

    if not changed_flag:
        break
    seat_mat = copy.deepcopy(new_mat)
    new_mat = copy.deepcopy(seat_mat)

total = 0
for i in range(len(new_mat)):
    for j in range(len(new_mat[0])):
        if new_mat[i][j] == "#":
            total += 1

print(total)