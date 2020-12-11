inst_list = []
with open("08.in", "r") as file:
    for l in file:
        l = l.strip().split()
        l[1] = int(l[1])
        inst_list.append(l)

#start accumulator at 0
inst = 0
acc = 0
executed = set()
while(True):
    if inst in executed:
        print(acc)
        break
    else:
        executed.add(inst)

    if inst_list[inst][0] == "acc":
        acc += inst_list[inst][1]
        inst += 1
    elif inst_list[inst][0] == "jmp":
        inst += inst_list[inst][1]
    else:
        inst += 1
