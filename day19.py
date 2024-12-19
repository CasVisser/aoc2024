import aocd, sys

inp = r"""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=19, year=2024)

### BEGIN SOLUTION

from collections import defaultdict
from functools import cache

part1 = part2 = 0

towels, patterns = inp.split("\n\n")
towels = [(t, len(t)) for t in towels.split(", ")]

@cache
def possible(pattern, start=0):
    if start >= len(pattern):
        return 1
    options = 0
    for t, l in towels:
        if pattern[start : start + l] == t:
            options += possible(pattern, start=start + l)
    return options

for pattern in patterns.split("\n"):
    part2 += possible(pattern)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=19, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=19, year=2024)
