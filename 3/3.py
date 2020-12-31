# Part 1
inputData = []
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        inputData.append(line.strip())


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

treeMaps = []
treeMaps.append(TreeMap(inputData, 1, 1))
treeMaps.append(TreeMap(inputData, 3, 1))
treeMaps.append(TreeMap(inputData, 5, 1))
treeMaps.append(TreeMap(inputData, 7, 1))
treeMaps.append(TreeMap(inputData, 1, 2))

treeMul = 0

for elem in treeMaps:
    treeCount = 0
    while elem.hasNext():
        if elem.next() == "#":
            treeCount += 1
    if treeMul == 0:
        treeMul = treeCount
    else:
        treeMul *= treeCount

print(treeMul)
