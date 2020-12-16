
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

print(fields)
print(main_ticket)
print(tickets)

valid_set = set()
for k in fields.keys():
    [valid_set.add(i) for i in range(fields[k][0], fields[k][1]+1)]
    [valid_set.add(i) for i in range(fields[k][2], fields[k][3]+1)]

invalids = []
for t in tickets:
    for i in range(len(t)):
        if t[i] not in valid_set:
            invalids.append(t[i])

print(sum(invalids))