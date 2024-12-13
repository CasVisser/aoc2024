import aocd, sys

inp = r"""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=13, year=2024)

### BEGIN SOLUTION

import re

def solve(ax, ay, bx, by, gx, gy):
    a = (gx - (bx * gy) / by) / (ax - (ay * bx) / by)
    b = (gy - a * ay) / by
    return 3 * round(a) + round(b) if abs(round(a) - a) < .01 and abs(round(b) - b) < .01 else 0

part1 = part2 = 0
for machine in inp.split("\n\n"):
    ax, ay, bx, by, gx, gy = map(int, re.findall(
            r".*A: X\+(\d+), Y\+(\d+).*B: X\+(\d+), Y\+(\d+).*X=(\d+), Y=(\d+)", 
            machine, 
            flags=re.DOTALL)[0])
    part1 += solve(ax, ay, bx, by, gx, gy)
    gx += 10000000000000
    gy += 10000000000000
    part2 += solve(ax, ay, bx, by, gx, gy)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=13, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=13, year=2024)
