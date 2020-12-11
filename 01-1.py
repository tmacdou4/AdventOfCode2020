seen = set()
with open("01-1.in", "r") as file:
    for l in file:
        current = int(l.strip())
        needed = 2020 - current
        if needed in seen:
            print(needed * current)
        else:
            seen.add(current)