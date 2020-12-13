import numpy as np

#Not used
def gcd(a,b):
    if a < b:
        t = a
        a = b
        b = t

    while a != 0 and b != 0:
        while a >= b:
            a = a - b
        t = a
        a = b
        b = t

    if a > 0:
        return a
    else:
        return b

#not used
def lcm_2(a,b):
    return a*b/gcd(a,b)

#not used
def lcm(a,b):

    og_a = a
    og_b = b

    while (a - b) != 0:
        if a > b:
            while a > b:
                b = b + og_b
        elif b > a:
            while b > a:
                a = a + og_a

    return a

#not used
def lcm_offset(a, a_off, b, b_off):

    og_a = a
    og_b = b

    while ((a-a_off) != (b-b_off)):
        if a-a_off > b-b_off:
            while a-a_off > b-b_off:
                b = b + og_b
        elif b-b_off > a-a_off:
            while b-b_off > a-a_off:
                a = a + og_a

    return a

#not used, fully brute force solution
def lcm_offset_array(nums, offs):

    og_nums = nums.copy()

    while not np.all((nums-offs)==(nums-offs)[0]):
        min = 100000000
        min_i = -1
        for i in range(len(nums)):
            if nums[i]-offs[i] < min:
                min = nums[i]
                min_i = i

        nums[min_i] += og_nums[min_i]

    return (nums-offs)[0]

#chinese remainder theorem
def crt(nums, offs):
    current = offs[0]
    for i in range(len(nums)-1):
        adder = np.prod(nums[:i+1])
        while(current % nums[i+1] != offs[i+1]):
            current += adder

    return current

#get input
with open("13.in", "r") as file:
    for i, l in enumerate(file):
        l = l.strip()
        if i == 0:
            ts=int(l)
        elif i == 1:
            timestamps = l

#clean up timestamps
timestamps = timestamps.split(",")
timestamps_np = np.zeros(len(timestamps)).astype(np.int)
for i in range(0, len(timestamps)):
    if timestamps[i] != 'x':
        timestamps_np[i] = int(timestamps[i])
timestamps = timestamps_np

offsets = np.arange(len(timestamps))

non_z = np.nonzero(timestamps)

nums = timestamps[non_z]
offs = offsets[non_z]

offs = offs%nums

remains = np.array(nums - offs)
remains[0] = 0
args = np.argsort(-nums)
nums = nums[args]
remains = remains[args]

print(crt(nums, remains))
