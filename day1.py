import aocd, sys

inp = r"""199
200
208
210
200
207
240
269
260
263"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=1, year=2024)

part1 = None
part2 = None

### BEGIN SOLUTION

from collections import defaultdict

part1 = part2 = 0

left = []
right = []
for line in inp.split("\n"):
    l, r = line.split("   ")
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()
count = defaultdict(int)
for l, r in zip(left, right):
    part1 += abs(l - r)
    count[r] += 1

for l in left:
    part2 += l * count[l]

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=1, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=1, year=2024)
