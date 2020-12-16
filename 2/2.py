# Part 1
inputData = []
with open("2/inputData.txt", "r") as inputDataData:
    for line in inputDataData:
        inputData.append(line.strip())

correctAmount = 0

for password in inputData:
    parameters = password.split()
    amounts = parameters[0].split("-")
    amounts = list(map(int, amounts))
    letter = parameters[1][0]
    password = parameters[2]
    charSum = 0
    for char in password:
        if char == letter:
            charSum += 1
    if charSum >= amounts[0] and charSum <= amounts[1]:
        correctAmount += 1

print(correctAmount)

# Part 2

correctAmount = 0

for password in inputData:
    parameters = password.split()
    locations = parameters[0].split("-")
    locations = list(map(int, locations))
    letter = parameters[1][0]
    password = parameters[2]
    if password[locations[0] - 1] == letter or password[locations[1] - 1] == letter:
        if password[locations[0] - 1] != password[locations[1] - 1]:
            correctAmount += 1

print(correctAmount)
