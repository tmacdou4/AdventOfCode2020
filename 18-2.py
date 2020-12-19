
def evaluate(s):
    out_nums = []
    op_stack = []

    nums = {"1","2","3","4","5","6","7","8","9"}
    i = 0
    while i < len(s):
        if s[i] in nums:
            out_nums.append(int(s[i]))
        elif s[i] == "(":
            stack = 1
            for j in range(i + 1, len(s)):
                if s[j] == "(":
                    stack += 1
                elif s[j] == ")":
                    stack -= 1
                    if stack == 0:
                        out_nums.append(evaluate(s[i + 1:j]))
                        i = j
                        break
        elif s[i] == "+":
            while len(op_stack) > 0:
                if op_stack[-1] == "+":
                    a = out_nums.pop()
                    b = out_nums.pop()
                    out_nums.append(a+b)
                    op_stack.pop()
                else:
                    break #just push to the stack

            op_stack.append(s[i])

        elif s[i] == "*":
            while len(op_stack) > 0:
                if op_stack[-1] == "+":
                    a = out_nums.pop()
                    b = out_nums.pop()
                    out_nums.append(a + b)
                    op_stack.pop()
                else:
                    a = out_nums.pop()
                    b = out_nums.pop()
                    out_nums.append(a * b)
                    op_stack.pop()

            op_stack.append(s[i])

        i += 1

    while len(op_stack) > 0:
        if op_stack[-1] == "+":
            a = out_nums.pop()
            b = out_nums.pop()
            out_nums.append(a + b)
            op_stack.pop()
        else:
            a = out_nums.pop()
            b = out_nums.pop()
            out_nums.append(a * b)
            op_stack.pop()

    return out_nums[-1]

total_sum = 0
with open("18.in", "r") as file:
    for l in file:
        l = l.strip().replace(" ", "")
        total_sum += evaluate(l)
print(total_sum)