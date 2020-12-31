# Part 1
inputData = []
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        inputData.append(int(line.strip()))

for i in range(0, len(inputData)):
    for j in range(i, len(inputData)):
        if(inputData[i] + inputData[j] == 2020):
            print(inputData[i], inputData[j])
            print(inputData[i]*inputData[j])

# Part 2
for i in range(0, len(inputData)):
    for j in range(i, len(inputData)):
        for k in range(j, len(inputData)):
            if (inputData[i] + inputData[j] + inputData[k] == 2020):
                print(inputData[i], inputData[j], inputData[k])
                print(inputData[i]*inputData[j]*inputData[k])
