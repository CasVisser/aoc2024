import aocd, sys

inp = r"""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=3, year=2024)

part1 = None
part2 = None

### BEGIN SOLUTION

import re

mul = lambda s: sum(int(n1) * int(n2) for n1, n2 in re.findall(r"mul\((\d+),(\d+)\)", s))
part1 = mul(inp) 
part2 = sum(mul(s) for s in re.findall(r"(?:^|do\(\))(.*?)(?:don't\(\)|$)", inp, flags=re.DOTALL))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=3, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=3, year=2024)
