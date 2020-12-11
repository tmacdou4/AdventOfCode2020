
with open("02.in", "r") as file:
    total_count = 0
    for l in file:
        line_list = l.strip().split()
        num_list = line_list[0].split("-")
        mini = int(num_list[0])
        maxi = int(num_list[1])
        char = line_list[1][0]
        password = line_list[2]

        count = 0
        for i in range(len(password)):
            if password[i] == char:
                count += 1

        if count >= mini and count <= maxi:
            total_count += 1

    print(total_count)