# Part 1
input = []
with open("1/input.txt", "r") as inputData:
    for line in inputData:
        input.append(int(line.strip()))

for i in range(0, len(input)):
    for j in range(i, len(input)):
        if(input[i] + input[j] == 2020):
            print(input[i], input[j])
            print(input[i]*input[j])

# Part 2
