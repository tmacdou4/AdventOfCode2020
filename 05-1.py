with open("05.in", "r") as file:
    max = 0
    for l in file:
        l = l.strip()
        row = 0
        col = 0
        for i in range(7):
            if l[i] == "B":
                row = row + 2**(6-i)
        for i in range(3):
            if l[7+i] == "R":
                col = col + 2**(2-i)
        id = row*8+col
        if id > max:
            max = id
    print(max)

