with open("06.in", "r") as file:
    set_list = []
    current_set = set()
    for l in file:
        if l == "\n":
            set_list.append(current_set)
            current_set = set()
        else:
            l = l.strip()
            for i in range(len(l)):
                current_set.add(l[i])
    set_list.append(current_set)

    final_sum = 0
    for s in set_list:
        final_sum += len(s)
    print(final_sum)