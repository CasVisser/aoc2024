import aocd, sys

inp = r"""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=2, year=2024)

part1 = None
part2 = None

### BEGIN SOLUTION

from itertools import pairwise

def safe(report, ascending, can_remove=False):
    for i, (l1, l2) in enumerate(pairwise(report)):
        if (
               (    ascending and (l2 - l1 <= 0 or l2 - l1 > 3))
            or (not ascending and (l2 - l1 >= 0 or l2 - l1 < -3))
            ):
            if can_remove:
                l1_removed = list(report)
                l1_removed.pop(i)
                l2_removed = list(report)
                l2_removed.pop(i + 1)
                return safe(l1_removed, ascending) or safe(l2_removed, ascending)
            return False
    return True


part1 = 0 # 463
part2 = 0 # not 493, 522, 516, 545

reports = [[int(n) for n in line.split(" ")] for line in inp.split("\n")]
for report in reports:
    part1 += 1 if safe(report, True) or safe(report, False) else 0
    part2 += 1 if safe(report, True, can_remove=True) or safe(report, False, can_remove=True) else 0

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=2, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=2, year=2024)
