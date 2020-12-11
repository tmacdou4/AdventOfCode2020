adapters = []
with open("10.in", "r") as file:
    for l in file:
        l = int(l.strip())
        adapters.append(l)

dev_adapter = max(adapters)+3
adapters.append(dev_adapter)
#Algorithm is probably a search tree?
#Using recursion, if it exceeds joltage and doesn't use all adapters,
#kick back up from the lowest level of recursion

adapters.sort()
print(adapters)

curr = 0
diff = {}
diff[1] = 0
diff[2] = 0
diff[3] = 0

for i in adapters:
    diff[i-curr] += 1
    curr = i

print(diff[1]*diff[3])






def next_adapter(l, curr, diffs):
    if len(l) == 0:
        return True, []
    for i in l:
        if 0 < i - curr <= 3:
            new_l = l.copy()
            new_l.remove(i)
            diffs.append(i-curr)
            end, diffs = next_adapter(new_l, i, diffs)
            if end:
                return True, diffs
    return False, diffs

#print(next_adapter(adapters, 0))