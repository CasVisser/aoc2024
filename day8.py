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
from itertools import combinations

antennas = defaultdict(list)
for y, line in enumerate(inp.split("\n")):
    for x, c in enumerate(line):
        if c == ".":
            continue
        antennas[c].append(complex(x, y))

w = inp.find("\n")
h = (len(inp) // w + 1) - 1
antinodes1 = set()
antinodes2 = set()
for xys in antennas.values():
    for xy1, xy2 in combinations(xys, 2):
        d = xy1 - xy2
        get_antinodes = lambda values: {xy
                                        for i in values 
                                        for xy in [xy1 + (d * i), xy2 - (d * i)]
                                        if 0 <= xy.real < w and 0 <= xy.imag < h}
        antinodes1 |= get_antinodes([1])
        antinodes2 |= get_antinodes(range(w))

part1 = len(antinodes1)
part2 = len(antinodes2)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=8, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=8, year=2024)
