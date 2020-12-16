# Part 1
inputData = []
with open("3/input.txt", "r") as inputDataData:
    for line in inputDataData:
        inputData.append(line.strip())


class TreeMap:
    def __init__(self, inputData):
        self.inputData = inputData
        self.x = 0
        self.y = 0

    def hasNext(self):
        return self.y < len(self.inputData) - 1

    def next(self):
        return True


a = 1
a += 1
print(a)
