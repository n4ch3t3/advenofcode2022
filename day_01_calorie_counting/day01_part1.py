max_calories = 0
elve_calories = 0

with open('input.txt') as f:
    for line in f:
        if line == '\n':
            if elve_calories > max_calories:
                max_calories = elve_calories
            elve_calories = 0
        else:
            elve_calories += int(line.rstrip())

print(max_calories)
