import aocd, sys

inp = r"""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=15, year=2024)

### BEGIN SOLUTION

def show(robot, grid):
    for y in range(h):
        for x in range(2 * w):
            if robot == complex(x, y):
                print("@", end="")
                continue
            print(grid[complex(x, y)], end="")
        print()

def move_if_possible(xy, grid, d):
    if xy not in grid:
        return xy, grid
    if grid[xy + d] == "#":
        return xy, grid
    if grid[xy + d] == ".":
        new_grid = grid.copy()
        new_grid[xy + d] = grid[xy]
        new_grid[xy] = grid[xy + d]
        return xy + d, new_grid
    if d in [1j, -1j]: 
        new_xy, new_grid = move_if_possible(xy + d, grid, d)
        if xy == new_xy:
            return xy, grid
        other_rock_half = xy + d + (1 if grid[xy + d] == "[" else -1)
        new_xy, new_grid = move_if_possible(other_rock_half, new_grid, d)
        if other_rock_half == new_xy:
            return xy, grid
    else:
        _, new_grid = move_if_possible(xy + d, grid, d)
    if new_grid[xy + d] == ".":
        new_grid[xy + d] = grid[xy]
        new_grid[xy] = "."
        return xy + d, new_grid
    return xy, grid

boxes, moves = inp.split("\n\n")
w = boxes.find("\n"); h = len(boxes) // w
grid = dict()
for y, line in enumerate(boxes.split("\n")):
    for x, c in enumerate(line):
        if c == "O":
            grid[complex(2 * x, y)] = "["
            grid[complex(2 * x + 1, y)] = "]"
            continue
        if c == "@":
            robot = complex(2 * x, y)
            c = "."
        grid[complex(2 * x, y)] = c
        grid[complex(2 * x + 1, y)] = c
moves = moves.replace("\n", "")

part1 = part2 = 0
move_to_d = {">": 1, "^": -1j, "<": -1, "v": 1j}
for move in moves:
    show(robot, grid)
    input(move)
    robot, grid = move_if_possible(robot, grid, move_to_d[move])

part2 = int(sum(xy.real + 100 * xy.imag for xy, c in grid.items() if c == "["))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=15, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=15, year=2024)
