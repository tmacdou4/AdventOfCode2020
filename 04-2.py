import re

passport_list = []
with open("04.in", "r") as file:
    current_passport = {}
    for l in file:
        if l == "\n":
            passport_list.append(current_passport)
            current_passport = {}
        else:
            item_list = l.strip().split()
            for item in item_list:
                current_passport[item.split(":")[0]] = item.split(":")[1]

    passport_list.append(current_passport)

    valid_count = 0
    for pp in passport_list:
        valid_sub_count = 0
        for k in pp.keys():
            if k == "byr":
                if 1920 <= int(pp["byr"]) <= 2002:
                    valid_sub_count += 1
            if k == "iyr":
                if 2010 <= int(pp["iyr"]) <= 2020:
                    valid_sub_count += 1
            if k == "eyr":
                if 2020 <= int(pp["eyr"]) <= 2030:
                    valid_sub_count += 1
            if k == "hgt":
                if pp["hgt"][-2:] == "in":
                    if 59 <= int(pp["hgt"][:-2]) <= 76:
                        valid_sub_count += 1
                elif pp["hgt"][-2:] == "cm":
                    if 150 <= int(pp["hgt"][:-2]) <= 193:
                        valid_sub_count += 1
            if k == "hcl":
                if re.fullmatch(r"#[a-f0-9]{6}", pp["hcl"]) != None:
                    valid_sub_count += 1
            if k == "ecl":
                if pp["ecl"] in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    valid_sub_count += 1
            if k == "pid":
                if re.fullmatch(r"[0-9]{9}", pp["pid"]) != None:
                    valid_sub_count += 1

        if valid_sub_count == 7:
            valid_count += 1

    print(valid_count)