
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
        fields = set(pp.keys())
        req_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        if req_fields.issubset(fields):
            valid_count += 1

    print(valid_count)