
lines = []

with open("day-3.txt", "r") as file:
    lines = [i.strip() for i in file]


# PART 1

total = 0
for line in lines:
    first = max([int(i) for i in line[:-1]])
    second = max([i for i in line[line.index(str(first))+1:]])
    # print(int(str(first) + str(second)))
    total += int(str(first) + str(second))

print("Sum of largest 2-digit numbers:", total)



# PART 2

total = 0
DIGITS = 12
for line in lines:
    digits = []
    for digits_remaining in range(DIGITS-1, -1, -1): # go backwards through the number of digits remaining

        if digits_remaining == 0: 
            digits_remaining = -len(line) # fix a bug where the slice of :-0 removes everything
        
        digit = str(max([int(j) for j in line[:-digits_remaining]])) # slices off the last digits_remaining digits to guarantee digits for the rest of the number
        
        line = line[line.index(digit)+1:] # remove the left hand side behind the current digit
        digits.append(digit)

    total += int("".join(digits))

print("Sum of largest 12-digit numbers:", total)

