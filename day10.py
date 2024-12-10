import aocd, sys

inp = r"""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=10, year=2024)

### BEGIN SOLUTION

from collections import defaultdict
from itertools import product

part1 = part2 = 0
grid = {complex(x, y): int(c) for y, line in enumerate(inp.split("\n"))
                         for x, c in enumerate(line)}
starts = set()
for xy, v in grid.items():
    if v != 0:
        continue
    starts.add(xy)
    q = {xy}
    seen = set()
    tops = set()
    while q:
        xy = q.pop()
        seen.add(xy)
        neighbors = {xy + d for d in [1, -1, 1j, -1j] 
                     if xy + d in grid and grid[xy + d] - grid[xy] == 1
                     and xy + d not in seen}
        tops |= {n for n in neighbors if grid[n] == 9}
        q |= neighbors
    part1 += len(tops)

def find_top(xy, seen):
    neighbors = {xy + d for d in [1, -1, 1j, -1j] 
                 if xy + d in grid and grid[xy + d] - grid[xy] == 1
                 and xy + d not in seen}
    res = len({n for n in neighbors if grid[n] == 9})
    for n in neighbors:
        if grid[n] != 9:
            res += find_top(n, seen.copy())
    return res

for xy in starts:
    part2 += find_top(xy, set())

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=10, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=10, year=2024)
