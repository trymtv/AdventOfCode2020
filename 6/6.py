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

# Part 2


def intersection(lst1, lst2):
    return set(lst1) & set(lst2)


groups = []
equalAnswers = None

for elem in inputData:
    if equalAnswers == None:
        equalAnswers = elem
    elif elem == "":
        groups.append(equalAnswers)
        equalAnswers = None
    else:
        equalAnswers = intersection(equalAnswers, elem)
groups.append(equalAnswers)


sum = 0
for elem in groups:
    sum += len(elem)

print(sum)
