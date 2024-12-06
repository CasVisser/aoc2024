import aocd, sys

inp = r"""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=6, year=2024)

### BEGIN SOLUTION

from collections import defaultdict

grid = {complex(x, y): c for y, line in enumerate(inp.split("\n"))
                         for x, c in enumerate(line)}
start = [xy for xy in grid if grid[xy] == "^"][0]
pos = start

d = -1j # start by going up
visited = set()
path = []
while True:
    visited.add(pos)
    path.append((pos, d))
    new_pos = pos + d
    if new_pos not in grid:
        break
    if grid[new_pos] != "#":
        pos = new_pos
        continue
    d *= 1j

part1 = len(visited) 

part2 = 0
new_obstacles = set()
for i in range(len(path)):
    pos, d = path[i]
    new_obstacle = pos + d
    if new_obstacle not in grid or grid[new_obstacle] == "#":
        continue 
    # Check if we enter a loop if the next cell were obstructed
    seen = set()
    pos = start
    d = -1j
    while True:
        seen.add((pos, d))
        new_pos = pos + d
        if new_pos not in grid:
            break
        if (new_pos, d) in seen:
            new_obstacles.add(new_obstacle)
            break
        if grid[new_pos] != "#" and new_pos != new_obstacle:
            pos = new_pos
            continue
        d *= 1j

part2 = len(new_obstacles)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=6, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=6, year=2024)
