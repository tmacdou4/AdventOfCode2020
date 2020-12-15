
spoken = []
with open("15.in", "r") as file:
    for i, l in enumerate(file):
        l = l.strip().split(",")
        spoken = l

for i in range(len(spoken)):
    spoken[i] = int(spoken[i])

for i in range(len(spoken), 2021):
    last_spoke = spoken[i-1]
    found = False
    for j in range(i-2, -1,-1):
        if last_spoke == spoken[j]:
            found = True
            spoken.append(i - (j+1))
            break

    if not found:
        spoken.append(0)

print(spoken[2018])
print(spoken[2019])
print(spoken[2020])