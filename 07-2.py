import re

contains_dict = {}
full_list = []
with open("07.in", "r") as file:
    for l in file:
        l = l.strip()
        l = re.split("bags|bag", l)
        new_l = []
        for w in l:
            w = w.strip()
            new_l.append(w)
        l = new_l
        new_l = []
        new_l.append(l[0])
        for i, w in enumerate(l):
            if i>0:
                if len(l[i]) == 1:
                    l.remove(l[i])
                else:
                    l[i] = l[i].split()
                    new_l.append(l[i][-3])
                    new_l.append(l[i][-2] + " " + l[i][-1])
        full_list.append(new_l)

#Making the dead-ends
for i in range(len(full_list)):
    if full_list[i][-1] == 'no other':
        full_list[i] = [full_list[i][0]]

#Building a dictionary of what bags (values) are contained in each bag (keys)
#multiples are repeated that number of times
for l in full_list:
    for i in range((len(l)//2)+1):
        if i == 0:
            contains_dict[l[0]] = []
        else:
            contains_dict[l[0]] = contains_dict[l[0]] + int(l[i*2-1]) * [l[i*2]]

current_list = contains_dict["shiny gold"]
prev_lens = []
for i in range(10):
    next_current_list = []
    for i in range(len(current_list)):
        next_current_list = next_current_list + contains_dict[current_list[i]]
    prev_lens.append(len(current_list))
    current_list = next_current_list

print(sum(prev_lens))