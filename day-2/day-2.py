


inputText = ""
with open("day-2.txt", "r") as file:
    inputText = file.readline().strip()

ranges = [i.split("-") for i in inputText.split(",")]

# Part 1

def check_invalid(num):
    if len(num)%2==1:
        return False, 0
    if int(num[:int(len(num)/2)]) == int(num[int(len(num)/2):]):
        return True, int(num)
    return False, 0



total = 0
for r in ranges:
    for i in range(int(r[0]), int(r[1])+1):
        v, add = check_invalid(str(i))
        if v:
            total += add
print("Sum invalid IDs:", total)




# Part 2


def check_invalid(num):
    if num == "" or len(num) < 2:
        return False, 0
    for i in range(2, len(num)+1):
        if len(num)%i!=0:
            continue
        first = int(num[:int(len(num)/i)])

        if all([first == x for x in [int(num[j*int(len(num)/i):(j+1)*int(len(num)/i)]) for j in range(1, i)]]):
            return True, int(num)
    return False, 0

total = 0
for r in ranges:
    for i in range(int(r[0]), int(r[1])+1):
        v, add = check_invalid(str(i))
        if v:
            total += add

print("Sum invalid IDs:", total)
