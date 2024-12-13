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
from sys import setrecursionlimit
from collections import defaultdict
from functools import cache
setrecursionlimit(10000)
from math import inf

def bins(goal, b, l=0, h=100):
    if l > h:
        return None
    guess = (l + h) // 2
    new_goal = goal - (guess * b)
    if new_goal == 0:
        return guess
    if new_goal.real > 0 and new_goal.imag < 0 or new_goal.real < 0 and new_goal.imag > 0:
        return None
    if new_goal.real > 0:
        return bins(goal, b, l=guess+1, h=h)
    if new_goal.real < 0:
        return bins(goal, b, l=l, h=guess-1)

part1 = part2 = 0
for machine in inp.split("\n\n"):
    a_x, a_y, b_x, b_y, x, y = map(int, re.findall(
            r".*A: X\+(\d+), Y\+(\d+).*B: X\+(\d+), Y\+(\d+).*X=(\d+), Y=(\d+)", 
            machine, 
            flags=re.DOTALL)[0])
    a = complex(a_x, a_y)
    b = complex(b_x, b_y)
    goal = complex(x, y)
    min_cost = inf
    for i in range(101):
        cur_goal = goal - i * a
        d_b = bins(cur_goal, b)
        if d_b is not None:
            min_cost = min(min_cost, 3 * i + d_b)
    if min_cost < inf:
        part1 += min_cost
        

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=13, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=13, year=2024)
