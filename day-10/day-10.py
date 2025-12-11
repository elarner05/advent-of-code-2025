lines = []

with open("day-10.txt") as file:
    lines = [line.strip().split(" ") for line in file]

indicators = [line[0] for line in lines]
buttons = [line[1:-1] for line in lines]
joltages = [line[-1:][0] for line in lines]

indicators = [[False if c=="." else True for c in list(machine)[1:-1] ] for machine in indicators]
buttons = [[[int(i) for i in "".join(list(b)[1:-1]).split(",")] for b in line] for line in buttons]
joltages = [[int(v) for v in "".join(list(machine)[1:-1]).split(",") ] for machine in joltages]


# Part 1, brute force method

def wanted_indices(wanted_indicator, current):
    wanted = []
    for i in range(len(wanted_indicator)):
        if wanted_indicator[i] != current[i]:
            wanted.append(i)
    return wanted
        
count = 0

memory = {}
def fewest_presses(wanted_indicator, current_indicator, buttons):

    wanted = wanted_indices(wanted_indicator, current_indicator)
    # use memory to prevent repeated searches
    mem_hash = hash((tuple(wanted_indicator), tuple(current_indicator), tuple([tuple(button) for button in buttons])))
    if mem_hash in memory:
        return memory[mem_hash]
    if len(wanted) == 0:
        return 0
    if len(buttons) == 0:
        return 20 # this was a bad route, return
    

    num_presses = [20]
    for i, button in enumerate(buttons):
        if any([want in button for want in wanted]):
            new_cur = current_indicator[:]
            for index in button:
                new_cur[index] = not new_cur[index] # flip the indicators
            num_presses.append(fewest_presses(wanted_indicator, new_cur, [b for b in buttons if b != button])) # add answer to recursive search

    memory[mem_hash] = 1 + min(num_presses) # add answer to memory
    return 1 + min(num_presses)

presses = 0
for i in range(len(lines)):
    memory.clear()
    presses += fewest_presses(indicators[i], [False for i in range(len(indicators[i]))], buttons[i])
print("Fewest presses (part 1):", presses)



# Part 2

# brute force does not work, use integer linear programming

#requires pulp
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, LpStatus, PULP_CBC_CMD

def fewest_presses_ilp(target, buttons):

    n = len(target)
    m = len(buttons)

    # Define ILP problem
    prob = LpProblem("MinButtonPresses", LpMinimize)

    # Define variables: number of presses for each button
    x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(m)]

    # Objective: minimize total presses
    prob += lpSum(x)

    # Constraints: for each target index, sum of button effects must equal target
    for i in range(n):
        prob += lpSum(x[j] for j in range(m) if i in buttons[j]) == target[i]

    # Solve
    prob.solve(PULP_CBC_CMD(msg=False))

    if LpStatus[prob.status] != "Optimal":
        return None  # No solution

    # Extract solution
    presses = [int(x[j].value()) for j in range(m)]

    return presses # Returns list[int] of button presses (minimum total presses)



presses = 0

for i in range(len(lines)):
    a = fewest_presses_ilp(joltages[i], [tuple(b) for b in buttons[i]])
    if a == None:
        print("no solutions!")
        # continue
    presses += sum(a)
print("Fewest presses (part 2):", presses)