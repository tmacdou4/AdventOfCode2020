import numpy as np

WP_NS = 1
WP_WE = -10
NS = 0
WE = 0

# dir = "E"
compass = {"N":0, "E":1, "S":2, "W":3}
rev_compass = {0:"N", 1:"E", 2:"S", 3:"W"}

with open("12.in", "r") as file:
    for l in file:
        l = l.strip()
        inst = l[0]
        value = int(l[1:])
        if inst == "N":
            WP_NS += value
        elif inst == "S":
            WP_NS -= value
        elif inst == "W":
            WP_WE += value
        elif inst == "E":
            WP_WE -= value

        elif inst == "F":
            for i in range(value):
                wp_rel_ns = WP_NS-NS
                wp_rel_we = WP_WE-WE

                NS = WP_NS
                WE = WP_WE

                WP_NS = WP_NS + wp_rel_ns
                WP_WE = WP_WE + wp_rel_we
        else:
            rots = int(value/90)

            wp_rel_ns = WP_NS - NS
            wp_rel_we = WP_WE - WE

            if inst == "R":
                for i in range(rots):
                    new_point = np.matmul(np.array([[0,-1],[1,0]]), np.array([[wp_rel_we], [wp_rel_ns]]))
                    wp_rel_we = new_point[0,0]
                    wp_rel_ns = new_point[1,0]

                WP_WE = WE + wp_rel_we
                WP_NS = NS + wp_rel_ns
            if inst == "L":
                for i in range(rots):
                    new_point = np.matmul(np.array([[0, 1], [-1, 0]]), np.array([[wp_rel_we], [wp_rel_ns]]))
                    wp_rel_we = new_point[0,0]
                    wp_rel_ns = new_point[1,0]

                WP_WE = WE + wp_rel_we
                WP_NS = NS + wp_rel_ns

print(WE,NS)
print(-WE+-NS)

