import aocd, sys

inp = r"""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=12, year=2024)

### BEGIN SOLUTION

from collections import defaultdict

part1 = part2 = 0
grid = {complex(x, y): c for y, line in enumerate(inp.split("\n"))
                         for x, c in enumerate(line)}
q = set(grid.keys())
while q:
    cur = q.pop()
    t = grid[cur]
    area = {cur}
    area_size = 1
    while True:
        area |= {xy + d for d in [1, -1, 1j, -1j] for xy in area 
                 if xy + d in grid and grid[xy + d] == t}
        if len(area) <= area_size:
            break
        area_size = len(area)
    q -= area
    perimeter = [xy + d for d in [1, -1, 1j, -1j] for xy in area if xy + d not in area]
    part1 += len(area) * len(perimeter)
    sides = 0
    for d in [1, -1, 1j, -1j]:
        per = {xy + d for xy in area if xy + d not in area}
        while per:
            sides += 1
            q2 = {per.pop()}
            while q2:
                q2 = {xy + d for d in [d*1j, -d*1j] for xy in q2 if xy + d in per}
                per -= q2
    part2 += len(area) * sides
            


### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=12, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=12, year=2024)
