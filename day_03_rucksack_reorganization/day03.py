from typing import Iterator
import string


def misplaced_item(rucksack: str) -> str:
    half = len(rucksack) // 2
    [letter] = set(rucksack[:half]).intersection(rucksack[half:])
    return letter


def badge(rucksack: str, *rucksacks: str) -> str:
    [letter] = set(rucksack).intersection(*rucksacks)
    return letter


def badges(*rucksacks: str) -> Iterator[str]:
    it = iter(rucksacks)
    for group in zip(it, it, it):
        yield badge(*group)


with open('/home/h4x0r/projects/adventofcode2022/day_03_rucksack_reorganization/input.txt') as f:
    rucksacks = [line.rstrip() for line in f]

priorities = {letter: i for i, letter in enumerate(string.ascii_letters, 1)}

print("Part 1:", sum(priorities[misplaced_item(r)] for r in rucksacks))

print("Part 2:", sum(priorities[badge] for badge in badges(*rucksacks)))
