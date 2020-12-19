
def evaluate(s):
    last_num = 0
    op = "+"
    i = 0
    while i < len(s):
        if s[i] == "+" or s[i] == "*":  # it's an operation
            op = s[i]
        else:
            if s[i] == "(":
                stack = 1
                for j in range(i+1, len(s)):
                    if s[j] == "(":
                        stack += 1
                    elif s[j] == ")":
                        stack -= 1
                        if stack == 0:
                            curr_num = evaluate(s[i+1:j])
                            i = j
                            break

            else: #it's a number
                curr_num = int(s[i])

            if op == "+":
                last_num += curr_num
            elif op == "*":
                last_num *= curr_num
        i += 1

    return last_num

total_sum = 0
with open("18.in", "r") as file:
    for l in file:
        l = l.strip().replace(" ", "")
        total_sum += evaluate(l)
print(total_sum)

#print(evaluate("1+(2*3)+(4*(5+6))"))