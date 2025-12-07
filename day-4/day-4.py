grid =[]
with open("day-4.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

# Part 1

def at(x, y, grid):
    if x < 0 or x > len(grid[0])-1 or y < 0 or y > len(grid)-1:
        return 0
    if grid[y][x] == "@":
        return 1
    return 0

def neighbours(x, y, grid):
    positions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    return sum([at(x+pos[0], y+pos[1], grid) for pos in positions])

n = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if neighbours(x, y, grid) < 4 and grid[y][x] == "@":
            n += 1
print("Rolls with less than four neighbours", n)


# Part 2


def at(x, y, grid):
    if x < 0 or x > len(grid[0])-1 or y < 0 or y > len(grid)-1:
        return 0
    if grid[y][x] == "@":
        return 1
    return 0

def neighbours(x, y, grid):
    positions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    return sum([at(x+pos[0], y+pos[1], grid) for pos in positions])

n = 0

removeable = []
running = True
while running:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if neighbours(x, y, grid) < 4 and grid[y][x] == "@":
                n += 1
                removeable.append((x, y))
    if len(removeable) == 0:
        running = False

    for pos in removeable:
        grid[pos[1]][pos[0]] = "."
    removeable = []
    
print("Total removable rolls:", n)