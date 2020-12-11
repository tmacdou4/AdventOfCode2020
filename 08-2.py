import copy

def change_one_inst(inst_list, index):

    if inst_list[index][0] == "jmp":
        inst_list[index][0] = "nop"
    else:
        inst_list[index][0] = "jmp"

    inst = 0
    acc = 0
    executed = set()
    while (True):
        if inst in executed:
            return False, acc
        else:
            executed.add(inst)

        if inst_list[inst][0] == "acc":
            acc += inst_list[inst][1]
            inst += 1
        elif inst_list[inst][0] == "jmp":
            inst += inst_list[inst][1]
        else:
            inst += 1

        if inst >= len(inst_list):
            return True, acc

inst_list = []
with open("08.in", "r") as file:
    for l in file:
        l = l.strip().split()
        l[1] = int(l[1])
        inst_list.append(l)

inst = 0
acc = 0
executed = set()
jmp_list=[]
nop_list=[]
while(True):
    if inst in executed:
        break
    else:
        executed.add(inst)

    if inst_list[inst][0] == "acc":
        acc += inst_list[inst][1]
        inst += 1
    elif inst_list[inst][0] == "jmp":
        jmp_list.append(inst)
        inst += inst_list[inst][1]
    else:
        nop_list.append(inst)
        inst += 1

change_list = jmp_list + nop_list
master_inst_list = inst_list
for inst in change_list:
    temp_inst_list = copy.deepcopy(master_inst_list)
    output, acc = change_one_inst(temp_inst_list, inst)
    if output:
        print(acc)