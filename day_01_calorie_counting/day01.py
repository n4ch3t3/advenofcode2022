import heapq

with open('input.txt') as f:
    calories = [[int(value) for value in elve.splitlines()]
                for elve in f.read().split('\n\n')]

print("Part 1:", max(sum(per_elf) for per_elf in calories))
print("Part 2:", sum(heapq.nlargest(3, (sum(per_elf) for per_elf in calories))))
