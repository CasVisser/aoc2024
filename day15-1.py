import aocd, sys

inp = r"""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=15, year=2024)

### BEGIN SOLUTION

def move_if_possible(xy, grid, d):
    if grid[xy + d] == "#":
        return xy, grid
    if grid[xy + d] == ".":
        new_grid = grid.copy()
        new_grid[xy + d] = grid[xy]
        new_grid[xy] = grid[xy + d]
        return xy + d, new_grid
    _, new_grid = move_if_possible(xy + d, grid, d)
    if new_grid[xy + d] == ".":
        new_grid[xy + d] = grid[xy]
        new_grid[xy] = "."
        return xy + d, new_grid
    return xy, grid

boxes, moves = inp.split("\n\n")
w = boxes.find("\n"); h = len(boxes) // w
robot = complex(boxes.find("@") % (w + 1), boxes.find("@") // (w + 1))
grid = {complex(x, y): c for y, line in enumerate(boxes.split("\n"))
                         for x, c in enumerate(line)}
grid[robot] = "."
moves = moves.replace("\n", "")

part1 = part2 = 0
move_to_d = {">": 1, "^": -1j, "<": -1, "v": 1j}
for move in moves:
    robot, grid = move_if_possible(robot, grid, move_to_d[move])

part1 = int(sum(xy.real + 100 * xy.imag for xy, c in grid.items() if c == "O"))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=15, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=15, year=2024)
