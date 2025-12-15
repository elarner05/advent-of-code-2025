from copy import deepcopy

presents = {} # format: index of present : 3x3 2D array of flags indicating its cell occupation
problems = [] # format: list of dicts, where "x" is width, "y" is height, and each index of present is connected to an amount in the grid

with open("day-12-presents.txt", "r") as file:
    present_num = 0
    cur=  [[_ for _ in range(3)] for _ in range(3)]
    i = 0
    for line in file:
        line = line.strip()
        if line == "":
            presents[present_num] = cur
            continue
        if line[0].isdigit():
            
            present_num = int(line[0])
            cur=  [[False for _ in range(3)] for _ in range(3)]
            i=0
            continue
        else:
            if i == 3: print("?")
            for j, ch in enumerate(list(line)):
                if ch == "#":
                    cur[i][j] = True
        i+=1
    presents[present_num] = cur

with open("day-12-trees.txt", "r") as file:
   
    for line in file:
        line = line.strip()
        l = {}
        l["x"] = int(line.split(":")[0].split("x")[0])
        l["y"] = int(line.split(":")[0].split("x")[1])
        for i, amount in enumerate(line.split(":")[1].strip().split(" ")):
            l[i] = int(amount)
        problems.append(l)


def unique_orientations(base):
    orients = []

    cur = deepcopy(base)
    for i in range(4):
        #rotation
        rot = [[False for _ in range(3)] for _ in range(3)]
        for y in range(3):
            for x in range(3):
                if cur[y][x]:
                    rot[x][y] = True
        for row in rot:
            row.reverse()
        
        orients.append(rot)

        #horizontal reflection
        ref = deepcopy(rot)
        for row in ref:
            row.reverse()
        orients.append(ref)

        #vertical reflection
        ref = deepcopy(ref)
        ref.reverse()
        orients.append(ref)

        cur = deepcopy(rot)

    for i in range(len(orients)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if all([all([orients[i][y][x] == orients[j][y][x] for x in range(3)]) for y in range(3)]): # equal
                orients.pop(i) # remove the copy
                break
    return orients

areas = [0 for _ in range(6)]

for pi in range(6):
    areas[pi] = sum(sum([1 if c else 0 for c in row]) for row in presents[pi])
    presents[pi] = unique_orientations(presents[pi])

# Rects
rects = [{"presents":[0,1,2], "dim":(3, 6)}]
shapes = [{"presents":[5,5], "shape":[[True, True, True, False],
                                    [True, True, True, True],
                                    [True, True, True, True],
                                    [False, True, True, True]]},
         {"presents":[2,2], "shape":[[False, True, True],
                                     [True, True, True],
                                     [True, True, True],
                                     [True, True, False]]}]



# Remaining space
spare_space = []
for problem in problems:
    s = problem["x"] * problem["y"]
    for i in range(6):
        s -= problem[i] * areas[i]
    spare_space.append(s)

# Statistics

print("Max empty space:", max(spare_space))
print("Min empty space:", min(spare_space))
print("Average:", sum(spare_space)/len(spare_space))
print("# of problems:", len(spare_space))
print("# below zero:", sum([0 if t >=0 else 1 for t in spare_space]))
print("\n: ANSWER :")
print("# of problems whose areas could fit into the total area:", sum([1 if t >=0 else 0 for t in spare_space])) ## This is the answer
print()


# The code after this is not used, the sample problems were not specific enough to require full checking

grid = []
width=0
height=0
def recursive_dfs(p0, p1, p2, p3, p4, p5, targetx=0, targety=0) -> bool:
    pass
    



possible_problems = []
for i, problem in enumerate(problems):
    if spare_space[i] < 0:
        continue
    grid = [[False for y in range(problem["x"])] for x in range(problem["y"])]
    width=problem["x"]
    height=[problem["y"]]
    solved = recursive_dfs(problem[0], problem[1], problem[2], problem[3], problem[4], problem[5])
    if solved:
        possible_problems.append(i)


# print("Solvable problems:", len(possible_problems))