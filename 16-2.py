import numpy as np

#Today is a little bit messy

save_tickets = False
ticket_up = False
save_fields = True
tickets = []

fields = dict()
with open("16.in", "r") as file:
    for i, l in enumerate(file):
        if ticket_up:
            main_ticket = [int(x) for x in l.strip().split(",")]
            ticket_up = False
        elif save_tickets:
            l = l.strip()
            tickets.append([int(x) for x in l.split(",")])
        elif save_fields:
            l = l.strip().split(":")
            if l[0] is not "":
                ranges = l[1].split(" or ")
                low_a = int(ranges[0].split("-")[0])
                high_a = int(ranges[0].split("-")[1])
                low_b = int(ranges[1].split("-")[0])
                high_b = int(ranges[1].split("-")[1])

                fields[l[0]] = [low_a, high_a, low_b, high_b]
            else:
                save_fields = False

        if l == "nearby tickets:\n":
            save_tickets = True
        elif l == "your ticket:\n":
            ticket_up = True

valid_set = set()
for k in fields.keys():
    [valid_set.add(i) for i in range(fields[k][0], fields[k][1]+1)]
    [valid_set.add(i) for i in range(fields[k][2], fields[k][3]+1)]

#find invalid tickets
invalid_tickets = []
for i, t in enumerate(tickets):
    for j in range(len(t)):
        if t[j] not in valid_set:
            invalid_tickets.append(i)

#remove invalid tickets
for i in range(len(invalid_tickets)-1, -1, -1):
    del tickets[invalid_tickets[i]]


possible = dict()
for k in fields.keys():
    possible[k] = np.ones(len(tickets[0]))

#now going through the numbers on each ticket, remove the fields from contention if there is 1 rule break for that
#field
tickets = [main_ticket] + tickets

for i in range(len(tickets)):
    for j in range(len(tickets[0])):
        for key in fields.keys():
            if not (fields[key][0] <= tickets[i][j] <= fields[key][1]) and not (fields[key][2] <= tickets[i][j] <= fields[key][3]):
                possible[key][j] = 0

#Now check across all the fields. It there's one option thats the one it must be!
#repeat this process because some options will only become available when others are removed
for h in range(len(tickets[0])):
    for i in range(len(tickets[0])):
        s = 0
        key = ""
        for k in fields.keys():
            if possible[k][i] == 1:
                s += 1
                key = k

        if s == 1:
            possible[key] = np.zeros(len(tickets[0]))
            possible[key][i] = 1

#departure field mask
mask = np.zeros(len(tickets[0]))
for key in possible.keys():
    if key[:9] == "departure":
        mask += possible[key]

#get the numbers from the target fields of the main ticket
prod = 1
for i in range(len(main_ticket)):
    if mask[i] == 1:
        prod *= main_ticket[i]

print(prod)


