
with open("02.in", "r") as file:
    total_count = 0
    for l in file:
        line_list = l.strip().split()
        num_list = line_list[0].split("-")
        first = int(num_list[0])
        second = int(num_list[1])
        char = line_list[1][0]
        password = line_list[2]

        print(first, second, char, password)

        if password[first-1] == char and password[second-1] != char:
            total_count += 1
        if password[first-1] != char and password[second-1] == char:
            total_count += 1

    print(total_count)