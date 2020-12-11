import copy

seat_mat = []
with open("11.in", "r") as file:
    for l in file:
        l = list(l.strip())
        seat_mat.append(l)

def is_valid(mat, row, col):
    valid = True
    if not (0 <= row < len(mat)):
        valid = False
    if not (0 <= col < len(mat[0])):
        valid = False
    return valid

def check_adj(mat, row, col):
    total_occup = 0

    #checking directions clockwise from the top left
    i=1
    while(True):
        if is_valid(mat, row-i, col-i):
            if mat[row - i][col - i] == "#":
                total_occup += 1
                break
            elif mat[row - i][col-i] == "L":
                break
            else:
                i += 1
        else:
            break

    i = 1
    while (True):
        if is_valid(mat, row - i, col):
            if mat[row - i][col] == "#":
                total_occup += 1
                break
            elif mat[row - i][col] == "L":
                break
            else:
                i += 1
        else:
            break

    i = 1
    while (True):
        if is_valid(mat, row - i, col + i):
            if mat[row - i][col + i] == "#":
                total_occup += 1
                break
            elif mat[row - i][col + i] == "L":
                break
            else:
                i += 1
        else:
            break

    i = 1
    while (True):
        if is_valid(mat, row, col - i):
            if mat[row][col - i] == "#":
                total_occup += 1
                break
            elif mat[row][col - i] == "L":
                break
            else:
                i += 1
        else:
            break

    i = 1
    while (True):
        if is_valid(mat, row, col + i):
            if mat[row][col + i] == "#":
                total_occup += 1
                break
            elif mat[row][col + i] == "L":
                break
            else:
                i += 1
        else:
            break

    i = 1
    while (True):
        if is_valid(mat, row+i, col - i):
            if mat[row+i][col - i] == "#":
                total_occup += 1
                break
            elif mat[row+i][col - i] == "L":
                break
            else:
                i += 1
        else:
            break

    i = 1
    while (True):
        if is_valid(mat, row + i, col):
            if mat[row + i][col] == "#":
                total_occup += 1
                break
            elif mat[row + i][col] == "L":
                break
            else:
                i += 1
        else:
            break

    i = 1
    while (True):
        if is_valid(mat, row + i, col+i):
            if mat[row + i][col+i] == "#":
                total_occup += 1
                break
            elif mat[row + i][col+i] == "L":
                break
            else:
                i += 1
        else:
            break

    return total_occup

new_mat = copy.deepcopy(seat_mat)

count = 1
while(True):
    changed_flag = False
    for i in range(len(new_mat)):
        for j in range(len(new_mat[0])):
            occup = check_adj(seat_mat, i, j)
            if seat_mat[i][j] is "L" and occup == 0:
                new_mat[i][j] = '#'
                changed_flag = True
            elif seat_mat[i][j] is "#" and occup > 4:
                new_mat[i][j] = "L"
                changed_flag = True

    if not changed_flag:
        break
    seat_mat = copy.deepcopy(new_mat)
    new_mat = copy.deepcopy(seat_mat)
    count += 1

total = 0
for i in range(len(new_mat)):
    for j in range(len(new_mat[0])):
        if new_mat[i][j] == "#":
            total += 1

print(total)