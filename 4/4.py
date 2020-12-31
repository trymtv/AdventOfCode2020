# Part 1
inputData = []
newPass = {}
with open("input.txt", "r") as inputFile:
    for line in inputFile:
        if line != "\n":
            for elem in line.split():
                keyPair = elem.strip().split(":")
                newPass[keyPair[0]] = keyPair[1]
        else:
            inputData.append(newPass)
            newPass = {}
    inputData.append(newPass)

requiredFields = {"byr": "", "iyr": "", "eyr": "",
                  "hgt": "", "hcl": "", "ecl": "", "pid": ""}
validCount = 0

for passport in inputData:
    validCount += 1
    for field in requiredFields:
        if not field in passport:
            validCount -= 1
            break

print(validCount)

# Part 2

# Create validation


def isValidByr(byr):
    try:
        return len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002
    except:
        return False


def isValidIyr(iyr):
    try:
        return len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020
    except:
        return False


def isValidEyr(eyr):
    try:
        return len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030
    except:
        return False


def isValidHgt(hgt):
    pair = []
    pair.append(hgt[: -2])
    pair.append(hgt[-2:])
    try:
        if pair[1] == "cm":
            return int(pair[0]) >= 150 and int(pair[0]) <= 193
        elif pair[1] == "in":
            return int(pair[0]) >= 59 and int(pair[0]) <= 76
    except:
        return False


def isValidHcl(hcl):
    return hcl[0] == "#" and len(hcl[1:]) == 6


validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def isValidEcl(ecl):
    return ecl in validEcl


def isValidPid(pid):
    try:
        return len(pid) == 9 and int(pid)
    except:
        return False


# Tie validation to fields

requiredFields["byr"] = lambda byr: isValidByr(byr)
requiredFields["iyr"] = lambda iyr: isValidIyr(iyr)
requiredFields["eyr"] = lambda eyr: isValidEyr(eyr)
requiredFields["hgt"] = lambda hgt: isValidHgt(hgt)
requiredFields["hcl"] = lambda hcl: isValidHcl(hcl)
requiredFields["ecl"] = lambda ecl: isValidEcl(ecl)
requiredFields["pid"] = lambda pid: isValidPid(pid)


validCount = 0

for passport in inputData:
    validCount += 1
    for field in requiredFields:
        if field in passport:
            if not requiredFields[field](passport[field]):
                validCount -= 1
                break
        else:
            validCount -= 1
            break

print(validCount)
