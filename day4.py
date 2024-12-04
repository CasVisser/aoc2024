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

grid = {complex(x, y): c for y, line in enumerate(inp.split("\n"))
                         for x, c in enumerate(line)}

# Directions: right, right up, up, left up, left, left down, down, right down
part1 = sum("XMAS" == "".join(grid[xy + d * i] for i in range(len("XMAS")) if xy + d * i in grid)
            for d in (1, 1 - 1j, -1j, -1 -1j, -1, -1 + 1j, 1j, 1 + 1j) 
            for xy in grid if grid[xy] == "X")

# Corners: (bottom right, top left), (bottom left, top right)
part2 = sum(all(set("MS") == set(grid[xy + d] for d in dirs if xy + d in grid) 
                for dirs in ((1 + 1j, -1 - 1j), (-1 + 1j, 1 - 1j))) 
            for xy in grid if grid[xy] == "A")

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=4, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=4, year=2024)
