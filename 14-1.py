
def update_with_mask(value, mask):
    binary = bin(value)
    binary = binary[2:]
    binary = ("0" * (len(mask) - len(binary))) + binary
    binary = list(binary)

    for i in range(len(mask)):
        if mask[i] == "0":
            binary[i] = "0"
        elif mask[i] == "1":
            binary[i] = "1"

    value = int("".join(map(str, binary)), 2)

    return value


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
            value = update_with_mask(value, mask)
            memory[addr] = value

total = 0
for k in memory.keys():
    total += memory[k]

print(total)



