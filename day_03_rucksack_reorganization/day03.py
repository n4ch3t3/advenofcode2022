import string

letters = string.ascii_letters
priority = {}
priority_value = 1
for letter in letters:
    priority[letter] = priority_value
    priority_value += 1

repeated_items = []

with open('/home/h4x0r/projects/adventofcode2022/day_03_rucksack_reorganization/input.txt') as f:
    rucksacks = [line.rstrip() for line in f]

for list_of_items in rucksacks:
    number_of_items = len(list_of_items)
    if number_of_items % 2 == 0:
        first_compartment = list_of_items[0:number_of_items//2]
        second_compartment = list_of_items[number_of_items//2:]
    else:
        first_compartment = list_of_items[0:number_of_items//2+1]
        second_compartment = list_of_items[number_of_items//2+1:]
    repeated = set(first_compartment).intersection(second_compartment)
    repeated_items.extend(repeated)

priority_sum = sum(priority[letter] for letter in repeated_items)

print(f'Priority sum: {priority_sum}')

