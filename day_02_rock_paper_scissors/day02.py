Scores = {
    'A': 1, #rock
    'B': 2, #paper
    'C': 3, #scissors
    'X': 1, #rock, lose
    'Y': 2, #paper, draw
    'Z': 3, #scissors, win
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

Scores2 = {
    'X': 0,  # lose
    'Y': 3,  # draw
    'Z': 6 # win
}

decision = {}

decision[('A', 'X')] = 'C'
decision[('A', 'Y')] = 'A'
decision[('A', 'Z')] = 'B'
decision[('B', 'X')] = 'A'
decision[('B', 'Y')] = 'B'
decision[('B', 'Z')] = 'C'
decision[('C', 'X')] = 'B'
decision[('C', 'Y')] = 'C'
decision[('C', 'Z')] = 'A'

# X lose, Y draw, Z win

with open('input.txt') as f:
    lines = f.readlines()

score_1 = 0
score_2 = 0

for line in lines:
    values = line.rstrip().split(' ')
    score_1 = score_1 + Scores[values[1]] + Scores[''.join(values)]
    score_2 = score_2 + Scores[decision[(values[0], values[1])]] + Scores2[values[1]]

print("Part 1:", score_1)
print("Part 2:", score_2)

