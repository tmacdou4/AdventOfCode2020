with open("06.in", "r") as file:
    set_list = []
    current_set = set()
    fresh_set = True
    for l in file:
        if l == "\n":
            set_list.append(current_set)
            current_set = set()
            fresh_set = True
        else:
            l = l.strip()
            if fresh_set == True:
                for i in range(len(l)):
                    current_set.add(l[i])
                fresh_set = False
            else:
                new_set = set()
                for i in range(len(l)):
                    new_set.add(l[i])
                current_set = current_set.intersection(new_set)

    set_list.append(current_set)

    final_sum = 0
    for s in set_list:
        final_sum += len(s)
    print(final_sum)