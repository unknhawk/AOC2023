def read(filename):
    with open(filename) as f:
        data = [str(line) for line in f.read().split("\n")]     # so cool
        return data


def clean_string(string, direction):
    new = string
    text_numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    if direction == "forward":
        for char in range(3, len(string)):          # less than three characters can't be a number
            for i in range(0, 9):
                temp = string[0:char].replace(text_numbers[i], numbers[i])
                if temp != string[0:char]:          # changed from the original
                    string = temp+string[char:]     # substitute string

    if direction == "backward":
        for char in reversed(range(0, len(string)-2)):
            for i in range(0, 9):
                temp = string[char:].replace(text_numbers[i], numbers[i])
                if temp != string[char:]:
                    string = string[:char]+temp

    # if direction == "backward":
    #     order = list(reversed(range(0, len(new)-2)))
    #
    # for j in order:
    #     for i in range(0, 9):
    #         pos = j
    #         if direction == "backward":
    #             start = j
    #             pos = len(new)
    #         temp = new[start:pos].replace(text_numbers[i], numbers[i])
    #         if temp != new[start:pos]:
    #             new = temp+new[pos:]
    #             break

    return string


def find_number(string, direction):
    order = range(0, len(string))
    if direction == "backward":
        order = reversed(order)

    for i in order:
        temp = string[i].isnumeric()
        if temp:       # quit as soon as you've found something
            number = string[i]
            break
    return number

instructions = read("input-long.txt")

result1 = list()
for i in range(0, len(instructions)):
    l = find_number(instructions[i], "forward")
    r = find_number(instructions[i], "backward")
    result1.append(int(l)*10+int(r))
print(sum(result1), "\n")

result2 = list()
for i in range(0, len(instructions)):
    temp = clean_string(instructions[i], "forward")
    l = find_number(temp, "forward")
    temp = clean_string(instructions[i], "backward")
    r = find_number(temp, "backward")
    result2.append(int(l)*10+int(r))
print(sum(result2))