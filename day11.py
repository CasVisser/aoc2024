import aocd, sys

inp = r"""125 17"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=11, year=2024)

### BEGIN SOLUTION

from collections import Counter

stones = Counter(map(int, inp.split(" ")))
for i in range(75):
    new_stones = Counter()
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
            continue
        s = str(stone)
        if len(s) % 2 == 0:
            new_stones[int(s[:len(s) // 2])] += count
            new_stones[int(s[len(s) // 2:])] += count
            continue
        new_stones[stone * 2024] += count
    stones = new_stones
    if i == 24:
        part1 = new_stones.total()
part2 = new_stones.total()

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=11, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=11, year=2024)
