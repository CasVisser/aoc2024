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

part1 = part2 = 0
w = inp.find("\n")
h = inp.count("\n") + 1
grid = {complex(x, y): c for y, line in enumerate(inp.split("\n"))
                         for x, c in enumerate(line)}
graph = defaultdict(set)
for y, line in enumerate(inp.split("\n")):
    for x, c in enumerate(line):
        if c == "#":
            continue
        if c == "S":
            start = complex(x, y)
        if c == "E":
            goal = complex(x, y)
        graph[complex(x, y)] = {complex(x, y) + d for d in [1, -1j, -1, 1j] if complex(x, y) + d in grid}

min_dist = defaultdict(lambda: w * h)
min_dist[start] = 0
q = [(0, start)]
while q:
    dist, pos = q.pop()
    for n in graph[pos]:
        if dist + 1 < min_dist[n]:
            min_dist[n] = dist + 1
            q.append((dist + 1, n))

skips = []
for y, line in enumerate(inp.split("\n")):
    for x, c in enumerate(line):
        if c == "#":
            continue
        cheats = {complex(x, y) + 2 * d for d in [1, -1j, -1, 1j]}
        for cheat in cheats:
            if cheat not in grid or grid[cheat] == "#":
                continue
            skip = min_dist[cheat] - min_dist[complex(x, y)] - 2
            if skip >= 100:
                part1 += 1

        cheats = {complex(x, y) + i * dx + (l - i) * dy for dx in (1, -1) for dy in (1j, -1j) for l in range(2, 21) for i in range(l + 1)}
        for cheat in cheats:
            if cheat not in grid or grid[cheat] == "#":
                continue
            skip = min_dist[cheat] - min_dist[complex(x, y)] - int(abs(cheat.real - x) + abs(cheat.imag - y))
            # if skip == 74:
                # print(f"{x=} {y=} {cheat=} {min_dist[complex(x, y)]=} {min_dist[cheat]=} {grid[cheat]=}")
            if skip >= 100:
                skips.append(skip)
                part2 += 1

from collections import Counter
t = Counter(skips)
for l, c in sorted(t.items()):
    print(f"{c} cheats save {l}")


### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=20, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=20, year=2024)
