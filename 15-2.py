
spoken = []
with open("15.in", "r") as file:
    for i, l in enumerate(file):
        l = l.strip().split(",")
        spoken = l

for i in range(len(spoken)):
    spoken[i] = int(spoken[i])

most_recent = {}
for i in range(len(spoken)-1):
    most_recent[spoken[i]] = i+1

print(most_recent)

last_spoke = spoken[len(spoken)-1]
for i in range(len(spoken)-1, 29999999):
    if last_spoke in most_recent.keys():
        new_spoke = i+1 - most_recent[last_spoke]
    else:
        new_spoke = 0
    most_recent[last_spoke] = i+1
    last_spoke = new_spoke

print(last_spoke)