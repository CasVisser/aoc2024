import aocd, sys

inp = r"""###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=20, year=2024)

### BEGIN SOLUTION

from collections import defaultdict
from heapq import heappop, heappush

w = inp.find("\n"); h = inp.count("\n") + 1
start = complex(inp.find("S") % (w + 1), inp.find("S") // (w + 1))
grid = {complex(x, y) for y, line in enumerate(inp.split("\n"))
                      for x, c in enumerate(line) if c != "#"}
graph = {xy: {xy + d for d in [1, -1j, -1, 1j] if xy in grid and xy + d in grid} for xy in grid}

min_dist = defaultdict(lambda: w * h)
min_dist[start] = 0
q = [(0, start)]
while q:
    dist, pos = heappop(q)
    for n in graph[pos]:
        if dist + 1 < min_dist[n]:
            min_dist[n] = dist + 1
            heappush(q, (dist + 1, n))

part1 = part2 = 0
for xy in grid:
    cheats = {(l, xy + i + (l - abs(i)) * dy) for dy in (1j, -1j) 
              for l in range(2, 21) for i in range(-l, l + 1) if xy + i + (l - abs(i)) * dy in grid}
    for l, cheat in cheats:
        if min_dist[cheat] - min_dist[xy] - l >= 100:
            if l == 2:
                part1 += 1
            part2 += 1

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=20, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=20, year=2024)
