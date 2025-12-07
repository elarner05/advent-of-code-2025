freshRanges = ""
with open("day-5-ranges.txt", "r") as file:
    freshRanges = [line.strip() for line in file]

freshRanges = [[int(val) for val in r.split("-")] for r in freshRanges]

checkIDs = []
with open("day-5-test-ids.txt", "r") as file:
    checkIDs = [line.strip() for line in file]


# Part 1
count = 0
for id in checkIDs:
    for r in freshRanges:
        id = int(id)
        if id >= r[0] and id <= r[1]:
            count+=1
            break

print(count)


# Part 2


# 1 2 3 4 5 6 7 8 9
# Case 1:
# 1 - 3   5 - 7

# Case 2
# 1 - 3
#     3 - 5

# Case 3
# 1 - 3
#       4 - 6

# Case 4
# 1     -     7
#     3 - 5


freshRanges.sort(key = lambda x:x[0])
answer_ranges = []

def overlap(r1, r2):
    if r1[0] > r2[0]: r1, r2 = r2, r1 # smallest first
    #                 overlap                              within                            beside
    return (r1[0] <= r2[1] and r1[1] >= r2[0]) or (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r1[1] +1 == r2[0])

def merge(r1, r2):
    return [min(r1[0], r2[0]), max(r1[1], r2[1])]

for i, r1 in enumerate(freshRanges):
    cur_range = r1
    for r2 in freshRanges[i+1:]:
        if overlap(cur_range, r2):
            cur_range = merge(cur_range, r2)
    
    for ans in answer_ranges:
        if overlap(cur_range, ans):
            break
    else:
        answer_ranges.append(cur_range)

freshRanges = answer_ranges

totalfresh = 0
for r in answer_ranges:
    totalfresh+=r[1]-r[0]+1
print(totalfresh)
