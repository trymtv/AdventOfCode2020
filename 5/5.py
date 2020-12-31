# Part 1
def passToRow(code, l, u):
    mid = l + (u - l) // 2
    if l == u:
        return l
    elif code[0] == "F":
        return passToRow(code[1:], l, mid)
    elif code[0] == "B":
        return passToRow(code[1:], mid+1, u)


def passToCol(code, l, u):
    mid = l + (u - l) // 2
    if l == u:
        return l
    elif code[0] == "L":
        return passToCol(code[1:], l, mid)
    elif code[0] == "R":
        return passToCol(code[1:], mid+1, u)


inputData = []
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        inputData.append(line.strip())

sortedInput = sorted(inputData)

for elem in sortedInput[:8]:
    print(passToRow(elem[:7], 0, 127), passToCol(elem[-3:], 0, 7))

print("\n")

# Chosse the biggest


# Part 2
hits = 0
current = sortedInput[0][:7]
rows = []
for elem in sortedInput:
    if elem[:7] == current:
        hits += 1
    else:
        if hits < 8:
            rows.append(current)
        current = elem[:7]
        hits = 1
if hits < 8:
    rows.append(current)

notMissing = []

for elem in sortedInput:
    if elem[:7] in rows:
        notMissing.append(elem)

for elem in notMissing:
    print(passToRow(elem[:7], 0, 127), passToCol(elem[-3:], 0, 7))
