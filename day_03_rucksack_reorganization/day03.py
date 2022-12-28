import string

def misplaced_item(rucksack: str) -> str:
    half = len(rucksack) // 2
    [letter] = set(rucksack[:half]).intersection(rucksack[half:])
    return letter

with open('/home/h4x0r/projects/adventofcode2022/day_03_rucksack_reorganization/input.txt') as f:
    rucksacks = [line.rstrip() for line in f]

priorities = {letter: i for i, letter in enumerate(string.ascii_letters, 1)}

priority_sum = sum(priorities[misplaced_item(r)] for r in rucksacks)

print(f'Priority sum: {priority_sum}')

