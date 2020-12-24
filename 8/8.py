# Part 1
inputData = []
with open("8/input.txt", "r") as inputFile:
    for line in inputFile:
        line = line.strip().split()
        inputData.append(line + [False])

operations = {}
accumilator = 0
op = 0
nextOp = inputData[0]


def incOp(num):
    global op
    op += 1


def acc(num):
    global accumilator
    accumilator += int(num)
    incOp(num)


def jmp(num):
    global op
    op += int(num)


operations["nop"] = incOp
operations["acc"] = acc
operations["jmp"] = jmp

while not inputData[op][2]:
    inputData[op][2] = True
    operations[inputData[op][0]](inputData[op][1])

print(accumilator)
