
def enumerate_floating(addr):
    addrs = []
    no_X = True
    for i in range(len(addr)):
        if addr[i] == "X":
            no_X = False
            cp_1 = addr.copy()
            cp_1[i] = "0"
            cp_2 = addr.copy()
            cp_2[i] = "1"
            addrs += enumerate_floating(cp_1) + enumerate_floating(cp_2)
            break

    if no_X:
        addrs += [addr]

    return addrs

def update_with_mask(addr, mask):
    #convert address to list of binary bits
    binary = bin(addr)
    binary = binary[2:]
    binary = ("0" * (len(mask) - len(binary))) + binary
    binary = list(binary)

    #Update with mask
    for i in range(len(mask)):
        if mask[i] == "1":
            binary[i] = "1"
        elif mask[i] == "X":
            binary[i] = "X"

    #enumerate addresses from floating
    addrs = enumerate_floating(binary)

    #convert list of binary bits to address
    addrs = [int("".join(map(str, x)), 2) for x in addrs]
    return addrs

mask = "0"
memory = {}
with open("14.in", "r") as file:
    for i, l in enumerate(file):
        l = l.strip().split()
        if l[0] == "mask":
            mask = l[-1]
        else:
            addr = int(l[0].split("[")[1].split("]")[0])
            value = int(l[-1])
            addrs = update_with_mask(addr, mask)
            for a in addrs:
                memory[a] = value

total = 0
for k in memory.keys():
    total += memory[k]

print(total)



