# Part 1
inputData = []
with open("3/input.txt", "r") as inputDataData:
    for line in inputDataData:
        inputData.append(line.strip())

print(len(inputData))


class TreeMap:
    def __init__(self, inputData, xSpeed, ySpeed):
        self.inputData = inputData
        self.x = 0
        self.y = 0
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def hasNext(self):
        return self.y < len(self.inputData)

    def next(self):
        self.x += self.xSpeed
        if self.x >= len(self.inputData[0]):
            self.x -= len(self.inputData[0])
        self.y += self.ySpeed
        return self.inputData[self.y-self.ySpeed][self.x-self.xSpeed]


newMap = TreeMap(inputData, 3, 1)
treeCount = 0
while newMap.hasNext():
    if newMap.next() == "#":
        treeCount += 1

print(treeCount)

# Part 2
