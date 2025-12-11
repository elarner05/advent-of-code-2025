lines = []

with open("day-11.txt", "r") as file:
    lines = [line.strip() for line in file]

connections = {line.split(":")[0]:line.split(":")[1].strip().split(" ") for line in lines}


# Part 1

visited = set(["you"])

def dfs(visited, current):
    if current == "out":
        return 1
    
    total = 0
    for c in connections[current]:
        if c in visited:
            continue
        visited.add(c)
        total += dfs(visited, c)
        visited.remove(c)
    
    return total


count = dfs(visited, "you")

print("Part 1 unique path count:", count)



# Part 2


from functools import lru_cache
# Use Least-Recently-Used Cache for the parameters, to significantly boost performance; searches will never be repeated
@lru_cache(None) # better than day-10 approach
def dfs(node, dac, fft):
    if node == "dac":
        dac = 1
    if node == "fft":
        fft = 1
    
    if node == "out":
        return 1 if (dac and fft) else 0

    total = 0
    for next_node in connections[node]:
        total += dfs(next_node, dac, fft)
    return total

count = dfs("svr", 0, 0)

print("Part 2 unique path count:",count)