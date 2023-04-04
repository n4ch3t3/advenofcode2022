with open('/home/h4x0r/projects/adventofcode2022/day_05_supply_stacks/test.txt') as f:
    lines = [line.rstrip() for line in f]

index_number_of_stacks = lines.index('') - 1
stacks_numbers = list(map(int, lines[index_number_of_stacks].split()))
