import aocd, sys

inp = r"""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=8, year=2024)

### BEGIN SOLUTION

from collections import defaultdict

part1 = part2 = 0
antennas = defaultdict(list)
for y, line in enumerate(inp.split("\n")):
    for x, c in enumerate(line):
        if c == ".":
            continue
        antennas[c].append(complex(x, y))

w = inp.find("\n")
h = (len(inp) // w + 1) - 1
from itertools import combinations
antinodes = set()
for _f, xys in antennas.items():
    for xy1, xy2 in combinations(xys, 2):
        d = xy1 - xy2
        antinodes |= {xy for xy in [xy1 + d, xy2 - d] if 0 <= xy.real < w and 0 <= xy.imag < h}

part1 = len(antinodes)

antinodes = set()
for _f, xys in antennas.items():
    for xy1, xy2 in combinations(xys, 2):
        d = xy1 - xy2
        antinodes |= {xy for i in range(100) for xy in [xy1 + (d * i), xy2 - (d * i)] if 0 <= xy.real < w and 0 <= xy.imag < h}

part2 = len(antinodes)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=8, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=8, year=2024)
