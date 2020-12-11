
target = 41682220
nums = []
with open("09.in", "r") as file:
    for l in file:
        l = int(l.strip())
        nums.append(l)

#starting from the first number, if it's less than the target, add the next number in the list
#if it goes over, remove the last number

ind_low=0
ind_high=0

while(True):
    if sum(nums[ind_low:ind_high]) < target:
        ind_high += 1
    elif sum(nums[ind_low:ind_high]) > target:
        ind_low += 1
    else:
        print(min(nums[ind_low:ind_high]) + max(nums[ind_low:ind_high]))
        break
