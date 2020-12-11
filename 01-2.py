seen_two_sums = dict()
with open("01-1.in", "r") as file:
    num_l = [int(l.strip()) for l in file]
    for i in num_l:
        needed_two_sum = 2020 - i
        if needed_two_sum in set(seen_two_sums.keys()):
            print(seen_two_sums[needed_two_sum] * i)
        else:
            for j in num_l:
                seen_two_sums[i+j] = i*j