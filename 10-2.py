import numpy as np

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
adapters = [0] + adapters

memory = np.zeros(len(adapters))
memory[97] = 0
memory[96] = 1
memory[95] = 1
#memoization
for i in range(len(adapters)-4, -1, -1):
    total = 0
    if adapters[i+1] - adapters[i] <= 3:
        total += memory[i+1]
    if adapters[i+2] - adapters[i] <= 3:
        total += memory[i+2]
    if adapters[i+3] - adapters[i] <= 3:
        total += memory[i+3]
    memory[i] = total

print(memory[0])
