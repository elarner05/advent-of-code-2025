

lines = []

with open("day-7.txt", "r") as file:
    lines = [list(line.strip()) for line in file]


def change_location(x, y, char):
    if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[0]):
        return False
    lines[y][x] = char
    return True


# Part 1


split_count = 0
for y in range(1, len(lines)):
    for x in range(len(lines[y])):
        char = lines[y][x]
        prev = lines[y-1][x]
        if prev == "|" or prev == "S":
            if char == ".":
                change_location(x, y, "|")
            elif char == "^":
                change_location(x-1, y, "|")
                change_location(x+1, y, "|")
                split_count+=1
            elif char == "|":
                pass
            else:
                print("Found:", char)
print("Number of splits:", split_count)


# Part 2


checked_locations = {}

def timeline_counter(x, y):
    if lines[y-1][x] == "S":
        return 1
    
    if (x, y) in checked_locations:
        return checked_locations[(x, y)] # return saved value for this timeline position
    
    left, right, up = 0, 0, 0
    if (x-1>=0 and lines[y][x-1]) == "^" and lines[y-1][x-1] == "|":
        left = timeline_counter(x-1, y-1)
    if (x+1<=len(lines[0])-1 and lines[y][x+1]) == "^" and lines[y-1][x+1] == "|":
        right = timeline_counter(x+1, y-1)
    if (lines[y-1][x] == "|"):
        up = timeline_counter(x, y-1)
    
    checked_locations[(x, y)] = left + right + up

    return left + right + up

num_timelines = 0

# go from the bottom of the graph and check the timeline backwards recursively
y = len(lines)-1
for x in range(len(lines[y])):
    if lines[y][x] == "|":
        num_timelines += timeline_counter(x, y)

print("Number of timelines:", num_timelines)