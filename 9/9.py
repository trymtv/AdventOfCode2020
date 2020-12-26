# Part 1
inputData = []
with open("9/input.txt", "r") as inputFile:
    for line in inputFile:
        inputData.append(int(line.strip()))


preambleLen = 25

target = 0

for index, elem in enumerate(inputData):
    hit = False
    if index >= 25:
        for numIndex, num in enumerate(inputData[index - 25: index]):
            diff = elem - num
            if diff in inputData[index - 25: index]:
                hit = True
                break
        if not hit:
            target = elem
            print(elem)


# Part 2

l = 0
r = 1
partialSum = inputData[0] + inputData[1]
while partialSum != target:
    if r == len(inputData):
        print("iob")
        break
    elif l == r:
        print("no hit")
        break
    else:
        if partialSum < target:
            r += 1
            partialSum += inputData[r]
        elif partialSum > target:
            partialSum -= inputData[l]
            l += 1
        if partialSum == target:
            orderedList = sorted(inputData[l:r+1])
            print(orderedList[0] + orderedList[-1])
