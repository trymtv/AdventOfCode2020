# Part 1

inputData = []
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        inputData.append(int(line.strip()))
inputData.append(0)

sortedList = sorted(inputData)

sortedList.append(sortedList[-1] + 3)

diffSums = [0, 0, 0, 0]

for index, elem in enumerate(sortedList):
    if index != len(sortedList)-1:
        diff = sortedList[index + 1] - elem
        diffSums[diff] += 1
    else:
        break

print(diffSums[1] * diffSums[3])


# Part 2

numOfChoises = [1]

reversedList = list(reversed(sorted(inputData)))

for i, e in enumerate(reversedList[1:]):
    numOfChoises.append(0)
    for subI, subE in reversed(list(enumerate(reversedList[:i+1]))):
        if subE - e <= 3:
            numOfChoises[-1] += numOfChoises[subI]
        else:
            break

print(numOfChoises[-1])
