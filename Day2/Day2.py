guide = open("strategy_guide.txt", "r")
guide = guide.readlines()

new_guide = []


for tip in guide:
    new_guide.append(tip.strip())

# === PART ONE === 

# score according to my choice
def score_single_round(guide):
    first_score = 0
    for tip in range(0, len(guide)):
        if guide[tip][2] == "X":
            first_score += 1
        elif guide[tip][2] == "Y":
            first_score += 2
        elif guide[tip][2] == "Z":
            first_score += 3
    
    return first_score

# score according to outcome of the round
def outcome_round(guide):
    second_score = 0
    for tip in range(0, len(guide)):
        if guide[tip][0] == "A": 
            if guide[tip][2] == "X": 
                second_score += 3
            elif guide[tip][2] == "Y": 
                second_score += 6
            elif guide[tip][2] == "Z": 
                second_score += 0
        elif guide[tip][0] == "B":
            if guide[tip][2] == "X":
                second_score += 0
            elif guide[tip][2] == "Y": 
                second_score += 3
            elif guide[tip][2] == "Z":
                second_score += 6
        elif guide[tip][0] == "C": 
            if guide[tip][2] == "X":
                second_score += 6
            elif guide[tip][2] == "Y": 
                second_score += 0
            elif guide[tip][2] == "Z":
                second_score += 3
    return second_score
        

# score totall 
first_one = score_single_round(new_guide)
second_one = outcome_round(new_guide)

result = int(first_one) + int(second_one)
#  print of the first part 
print(result)


# === PART TWO === 

def secret_strategy(guide):
    third_score = 0
    for tip in range(0, len(guide)):
        if guide[tip][0] == "A": 
            if guide[tip][2] == "X":
                third_score += 0  # points for defeat
                third_score += 3  # points for choosing Scrissors
            elif guide[tip][2] == "Y": 
                third_score += 3  # points for draw
                third_score += 1  # points for Rock
            elif guide[tip][2] == "Z": 
                third_score += 6  # points for win
                third_score += 2  # points for choosing Paper
        elif guide[tip][0] == "B": 
            if guide[tip][2] == "X":
                third_score += 0  # points for defeat
                third_score += 1  # points for Rock
            elif guide[tip][2] == "Y": 
                third_score += 3  # points for draw
                third_score += 2  # points for choosing Paper 
            elif guide[tip][2] == "Z":
                third_score += 6  # points for win
                third_score += 3  # points for choosing Scrissors
        elif guide[tip][0] == "C": 
            if guide[tip][2] == "X":
                third_score += 0  # points for defeat
                third_score += 2  # points for choosing Paper
            elif guide[tip][2] == "Y": 
                third_score += 3  # points for draw
                third_score += 3  # points for choosing Scrissors
            elif guide[tip][2] == "Z":
                third_score += 6  # points for win
                third_score += 1  # points for Rock
    return third_score

result = secret_strategy(new_guide)
print (result)