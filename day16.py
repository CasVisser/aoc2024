import aocd, sys

inp = r"""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=16, year=2024)

### BEGIN SOLUTION

from collections import defaultdict
from heapq import heappush, heappop
from math import inf

grid = {complex(x, y): c for y, line in enumerate(inp.split("\n"))
                         for x, c in enumerate(line)}
w = inp.find("\n"); h = inp.count("\n") + 1
start = complex(1, h - 2)
goal  = complex(w - 2, 1)
q = [(0, 0, {start}, start, 1)] # dist, counter, path, pos, dir
dist = defaultdict(lambda: inf)
dist[(start, 1)] = 0
counter = 0
paths = []
while q:
    cur_dist, _, path, pos, d = heappop(q)
    if pos not in grid or grid[pos] == "#":
        continue
    if pos == goal:
        paths.append((cur_dist, path))
    neighbors = [(1, pos + d, d)] + [(1001, pos + new_d, new_d) for new_d in [d * 1j, d * -1j]]
    for cost, new_pos, new_d in neighbors:
        if new_pos not in grid or grid[new_pos] == "#":
            continue
        new_dist = cur_dist + cost
        if new_dist != inf and new_pos not in path and new_dist <= dist[(new_pos, new_d)]:
            dist[(new_pos, new_d)] = new_dist
            counter += 1
            heappush(q, (new_dist, counter, path | {new_pos}, new_pos, new_d))

part1 = min(dist[(goal, d)] for d in [1, -1j, -1, 1j])
part2 = len(set.union(*(path for path_dist, path in paths if path_dist == part1 and goal in path)))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=16, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=16, year=2024)
