"""
Day 4: Camp Cleanup
"""
import re

PATTERN = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


with open('/home/h4x0r/projects/adventofcode2022/day_04_camp_cleanup/input.txt') as f:
    pairs = [line.rstrip() for line in f]


def part1(pairs):
    count = 0
    for pair in pairs:
        a1, a2, b1, b2 = map(int, re.match(PATTERN, pair).groups())
        if a1 <= b1 and a2 >= b2 or a1 >= b1 and a2 <= b2:
            count += 1
    return count


def part2(pairs):
    count = 0
    for pair in pairs:
        a1, a2, b1, b2 = map(int, re.match(PATTERN, pair).groups())
        if a1 <= b2 and a2 >= b1:
            count += 1
    return count

print("Part 1:", part1(pairs))
print("Part 2:", part2(pairs))


