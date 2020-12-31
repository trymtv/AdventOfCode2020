import re


# Part 1
inputData = {}
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        line = re.sub(" bags| bag", "", line)
        line = re.split(" contain |, ", line.strip("\n."))
        inputData[line[0]] = line[1:]


validBags = set()
potentialBags = ["shiny gold"]
while potentialBags != []:
    current = potentialBags.pop()
    for bag in inputData:
        for contained in inputData[bag]:
            if current in contained:
                validBags.add(bag)
                if not current in potentialBags:
                    potentialBags.append(bag)

print(len(validBags))
# Part 2


def numberOfSubBags(bag):
    if not "no other" in inputData[bag]:
        sum = 1
        for sub in inputData[bag]:
            sum += int(sub[0]) * numberOfSubBags(sub[2:])
        return sum
    else:
        return 1


print(numberOfSubBags("shiny gold") - 1)
