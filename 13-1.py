
import math
with open("13.in", "r") as file:
    for i, l in enumerate(file):
        l = l.strip()
        if i == 0:
            ts=int(l)
        elif i == 1:
            info = l


info = info.split(",")
print(ts)
print(info)

min_partial = 1
min_partial_i = -1
for i, x in enumerate(info):
    if x == "x":
        pass
    else:
        x = int(x)
        if math.ceil(ts/x) - ts/x < min_partial:
            min_partial = math.ceil(ts/x) - ts/x
            min_partial_i = i

print(float(info[min_partial_i]) * min_partial * float(info[min_partial_i]))

print(float(info[min_partial_i]))
print(float(min_partial))
