# Part 1
inputData = []
with open("6/input.txt", "r") as inputFile:
    for line in inputFile:
        inputData.append(line.strip())

answerSet = set()
groups = []

for elem in inputData:
    if elem != "":
        for char in elem:
            answerSet.add(char)
    else:
        groups.append(answerSet)
        answerSet = set()
groups.append(answerSet)

sum = 0
for answers in groups:
    sum += len(answers)

print(sum)
