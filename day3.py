import aocd, sys

inp = r"""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=3, year=2024)

part1 = None
part2 = None

### BEGIN SOLUTION

part1 = 0

# while len(inp) > 3:
#     inp = inp[inp.find("mul(") + 4:]
#     n1 = inp[:inp.find(",")]
#     inp = inp[inp.find(",") + 1:]
#     if n1.isnumeric():
#         n1 = int(n1)
#     else:
#         continue
#     n2 = inp[:inp.find(")")]
#     inp = inp[inp.find("mul("):]
#     if n2.isnumeric():
#         n2 = int(n2)
#         print(f"{n1=} {n2=}")
#         part1 += n1 * n2
#     else:
#         continue

import re

for mul in re.findall(r"mul\(\d+,\d+\)", inp):
    n1, n2 = map(int, mul[4:-1].split(","))
    part1 += n1 * n2

# part2 = 0
# while True:
#     next_dont = inp.find("don't()")
#     s = inp[:next_dont]
#     for mul in re.findall(r"mul\(\d+,\d+\)", s):
#         n1, n2 = map(int, mul[4:-1].split(","))
#         print(f"{n1=} {n2=}")
#         part2 += n1 * n2
#     next_do = inp[next_dont:].find("do()") + 4
#     inp = inp[next_dont + next_do:]
#     if len(inp) < 6:
#         break

part2 = 0
for s in re.findall(r"(?:^|do\(\))(.*?)(?:don't\(\)|$)", inp.replace("\n", "")):
#     print(s)
    for mul in re.findall(r"mul\(\d+,\d+\)", s):
        n1, n2 = map(int, mul[4:-1].split(","))
        part2 += n1 * n2

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=3, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=3, year=2024)
