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

grid = {complex(x, y): c for y, line in enumerate(inp.split("\n"))
                         for x, c in enumerate(line)}
start = [xy for xy in grid if grid[xy] == "^"][0]

def walk(grid):
    d = -1j # start by going up
    seen = set()
    pos = start
    while pos in grid and (pos, d) not in seen:
        seen.add((pos, d))
        new_pos = pos + d
        if grid.get(new_pos) == "#":
            d *= 1j
            continue
        pos = new_pos
    return {pos for pos, _ in seen}, (pos, d) in seen

visited, _ = walk(grid)
part1 = len(visited) 
part2 = sum(walk(grid | {pos: "#"})[1] for pos in visited)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=6, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=6, year=2024)
