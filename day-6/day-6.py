inputText = []
with open("day-6.txt", "r") as file:
    inputText = [line.strip() for line in file]


# Part 1

lines = [[w for w in line.strip().split(" ") if w] for line in inputText]
nums = lines[:-1]
ops = lines[len(lines)-1]


total = 0
for i in range(len(ops)):
    if (ops[i]) == "+":
        inner = 0
        for j in range(len(nums)):
            inner += int(lines[j][i])

        total += inner
    elif (ops[i]) == "*":
        inner = 1
        for j in range(len(nums)):
            inner *= int(lines[j][i])

        total += inner
    else:
        print("Strange?:", ops[i])

print("Part 1:", total)


# Part 2


lines = [[ch for ch in line] for line in inputText]

nums = lines[:-1]
ops = lines[len(lines)-1]

total = 0
cur_nums = []
op = ops[0]

for i, ch in enumerate(ops):

    if ch == " " or i == 0:
        n = ""
        for j in range(len(nums)):
            n += nums[j][i]
        cur_nums.append(n)
    
    else:
        if (op) == "+":
            inner = 0
            for j in range(len(cur_nums)-1):
                inner += int(cur_nums[j].strip())

            total += inner
        elif (op) == "*":
            inner = 1
            for j in range(len(cur_nums)-1):
                inner *= int(cur_nums[j].strip())

            total += inner
        else:
            print("Strange?:", ops[i])
        

        cur_nums = []
        op = ch

        n = ""
        for j in range(len(nums)):
            n += nums[j][i]
        cur_nums.append(n)

if (op) == "+":
    inner = 0
    for j in range(len(cur_nums)):
        inner += int(cur_nums[j].strip())

    total += inner
elif (op) == "*":
    inner = 1
    for j in range(len(cur_nums)):
        inner *= int(cur_nums[j].strip())

    total += inner
else:
    print("Strange?:", ops[i])

print("Part 2:", total)
