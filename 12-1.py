

NS = 0
WE = 0
dir = "E"
compass = {"N":0, "E":1, "S":2, "W":3}
rev_compass = {0:"N", 1:"E", 2:"S", 3:"W"}
with open("12.in", "r") as file:
    for l in file:
        l = l.strip()
        inst = l[0]
        value = int(l[1:])
        if inst == "N":
            NS += value
        elif inst == "S":
            NS -= value
        elif inst == "W":
            NS += value
        elif inst == "E":
            NS -= value

        elif inst == "F":
            if dir == "N":
                NS += value
            if dir == "S":
                NS -= value
            if dir == "W":
                NS += value
            if dir == "E":
                NS -= value

        else:
            rots = value/90
            if inst == "R":
                dir = rev_compass[(compass[dir] + rots)%4]
            if inst == "L":
                dir = rev_compass[(compass[dir] - rots)%4]

print(WE, NS)

