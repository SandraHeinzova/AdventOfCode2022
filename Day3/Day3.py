
priority = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4, 
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26, 
    
    
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30, 
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}
with open("rucksacks.txt", "r") as rucksacks:
   rucksacks = rucksacks.readlines()
sum = 0
sum2 = 0
items = []
for x in rucksacks:
    items.append(x.strip())

# === PART ONE ===

# split rucksack into two compartments

for item in items:
    x = len(item)
    first_half = slice(0, x//2)
    second_half = slice(x//2, x)
    #  what letter is common for both parts of each rucksack
    for x in range(0, len(item[first_half])):
        if item[first_half][x] in item[second_half]:
            shared = item[first_half][x]
            convert_priority = priority[shared]
            # print(convert_priority)    test print
    sum += convert_priority

# print of the result of the first part
print(sum)

# # === PART TWO ===
groupsOfThree = []
#  make groups of three 
for i in range(0, len(items), 3):
    groupsOfThree.append(items[i:i + 3])
    

    
    
for a in range(0, 100):
    # print(groupsOfThree[a][0])  # control print
    for z in range (0, len(groupsOfThree[a][0])):
        # print(z)
        if groupsOfThree[a][0][z] in groupsOfThree[a][1]:
            if groupsOfThree[a][0][z] in groupsOfThree[a][2]:
                # print(groupsOfThree[a][0][z])  # control print
                shared2 = groupsOfThree[a][0][z]
                convert_priority2 = priority[shared2]
            # print(convert_priority)    test print
    sum2 += convert_priority2

#  print of the result of the second part
print(sum2)