Scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}

with open('input.txt') as f:
    lines = f.readlines()

score = 0

for line in lines:
    values = line.rstrip().split(' ')
    score = score + Scores[values[1]] + Scores[''.join(values)]

print(score)
