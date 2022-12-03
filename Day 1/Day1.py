calories = open("calories.txt", "r")
calories = calories.readlines()

new_calories = []

for num in calories:
    new_calories.append(num.strip())

max_sum = 0
all_sums = []

for num in new_calories:
    if num != "":
        num = int(num)
        max_sum += num           
    elif num == "":
        all_sums.append(max_sum)
        max_sum = 0
        
# answer to part 1
print(max(all_sums))
            
all_sums.sort(reverse=True)
top_three = (all_sums[0]+all_sums[1]+all_sums[2])

# answer to part 2
print(top_three)           
        

    

       
    