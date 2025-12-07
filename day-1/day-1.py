
rotations = []
with open("day-1.txt", "r") as file:
    rotations = [line.strip() for line in file]

# Part 1

rot = 50
ans = 0
for move in rotations:
    print(move)
    direction = move[0]
    amount = int(move[1:])
    if direction == "R":
        rot+=amount
    elif direction == "L":
        rot-=amount
    else:
        print("What the ...")
        print()
        print(direction)
        print()
        break

    rot %= 100

    if rot == 0:
        ans+=1
print("Part 1:", ans)


rot = 50
ans = 0
for move in rotations:
    # print(move)
    direction = move[0]
    amount = int(move[1:])
    for i in range(amount):
        if direction == "R":
            rot+=1
        elif direction == "L":
            rot-=1
        rot %= 100
        if rot == 0:
            ans+=1

print("Part 2:", ans)
