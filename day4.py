import aocd, sys

inp = r"""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=4, year=2024)

part1 = None
part2 = None

### BEGIN SOLUTION

part1 = 0

xmas = "XMAS"

grid = [list(line) for line in inp.split("\n")]
h = len(grid)
w = len(grid[0])

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "X":
            # right
            for i in range(1, len(xmas)):
                new_x = x + i
                if new_x >= w:
                    break
                if grid[y][new_x] != xmas[i]:
                    break
            else:
                part1 += 1
            # left
            for i in range(1, len(xmas)):
                new_x = x - i
                if new_x < 0:
                    break
                if grid[y][new_x] != xmas[i]:
                    break
            else:
                part1 += 1
            # up
            for i in range(1, len(xmas)):
                new_y = y - i
                if new_y < 0:
                    break
                if grid[new_y][x] != xmas[i]:
                    break
            else:
                part1 += 1
            # right
            for i in range(1, len(xmas)):
                new_y = y + i
                if new_y >= h:
                    break
                if grid[new_y][x] != xmas[i]:
                    break
            else:
                part1 += 1

            # diag / up
            for i in range(1, len(xmas)):
                new_x = x + i
                new_y = y - i
                if new_x >= w or new_y < 0:
                    break
                if grid[new_y][new_x] != xmas[i]:
                    break
            else:
                part1 += 1
            # diag / down
            for i in range(1, len(xmas)):
                new_x = x - i
                new_y = y + i
                if new_x < 0 or new_y >= h:
                    break
                if grid[new_y][new_x] != xmas[i]:
                    break
            else:
                part1 += 1
            # diag \ up
            for i in range(1, len(xmas)):
                new_x = x - i
                new_y = y - i
                if new_x < 0 or new_y < 0:
                    break
                if grid[new_y][new_x] != xmas[i]:
                    break
            else:
                part1 += 1
            # diag \ down
            for i in range(1, len(xmas)):
                new_x = x + i
                new_y = y + i
                if new_x >= w or new_y >= h:
                    break
                if grid[new_y][new_x] != xmas[i]:
                    break
            else:
                part1 += 1

part2 = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c != "A":
            continue

        tl = (x - 1, y - 1)
        tr = (x + 1, y - 1)
        bl = (x - 1, y + 1)
        br = (x + 1, y + 1)

        invalid = False
        for coords in [tl, tr, bl, br]:
            if not (0 <= coords[0] < w and 0 <= coords[1] < h):
                invalid = True
        if invalid:
            continue

        if (
            ((grid[tl[1]][tl[0]] == "M" and grid[br[1]][br[0]] == "S") or (grid[tl[1]][tl[0]] == "S" and grid[br[1]][br[0]] == "M"))
            and ((grid[tr[1]][tr[0]] == "M" and grid[bl[1]][bl[0]] == "S") or (grid[tr[1]][tr[0]] == "S" and grid[bl[1]][bl[0]] == "M"))
            ):
            part2 += 1

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=4, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=4, year=2024)
