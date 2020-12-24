import copy

# Part 1
inputData = []
with open("8/input.txt", "r") as inputFile:
    for line in inputFile:
        line = line.strip().split()
        inputData.append(line + [False])

inputCopy = copy.deepcopy(inputData)
operations = {}
accumilator = 0
op = 0


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


def execute():
    while not inputData[op][2]:
        inputData[op][2] = True
        operations[inputData[op][0]](inputData[op][1])
        if op == len(inputData):
            return True


execute()
print(accumilator)

# Part 2


def resetInput():
    global inputData
    inputData = copy.deepcopy(inputCopy)


resetInput()
nopJmpPair = ["nop", "jmp"]
for index, operation in enumerate(inputData):
    op = 0
    accumilator = 0
    if operation[0] in nopJmpPair:
        inputData[index][0] = "jmp" if operation[0] == "nop" else "nop"
        if execute():
            print(accumilator)
            break
        else:
            resetInput()
