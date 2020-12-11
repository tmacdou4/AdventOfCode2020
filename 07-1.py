import re

contains_dict = {}
contained_in = {}
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
                    new_l.append(l[i][-2] + " " + l[i][-1])
        full_list.append(new_l)

for l in full_list:
    for i in range(len(l)):
        if i == 0:
            contains_dict[l[i]] = set()
        else:
            contains_dict[l[0]].add(l[i])

            if l[i] not in contained_in.keys():
                contained_in[l[i]] = set()
            contained_in[l[i]].add(l[0])

diff_colours = set()
current_list = list(contained_in["shiny gold"])
for i in range(10):
    next_current_list = []
    for i in range(len(current_list)):
        diff_colours.add(current_list[i])
        if current_list[i] in contained_in.keys():
            next_current_list = next_current_list + list(contained_in[current_list[i]])
    print(current_list)
    current_list = next_current_list

print(diff_colours)
print(len(diff_colours))