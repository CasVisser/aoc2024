import aocd, sys

inp = r"""029A
980A
179A
456A
379A"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=21, year=2024)

### BEGIN SOLUTION

from collections import Counter, defaultdict
from itertools import pairwise

part1 = part2 = 0

kp1 = "789456123 0A"
kp2 = " ^A<v>"
dists = defaultdict(lambda: defaultdict(dict))

for kp in [kp1, kp2]:
    for i, c1 in enumerate(kp):
        for j, c2 in enumerate(kp[i:]):
            xi = i % 3
            yi = i // 3
            xj = (i + j) % 3
            yj = (i + j) // 3
            d = abs(xi - xj) + abs(yi - yj)
            dists[kp][c1][c2] = (d, "v" * (yj - yi) + "<" * (xi - xj) + ">" * (xj - xi))
            dists[kp][c2][c1] = (d, "^" * (yj - yi) + ">" * (xi - xj) + "<" * (xj - xi))

for code in inp.split("\n"):
    n = int(code[:-1])
    code = "A" + code
    seq1 = "A"
    for c1, c2 in pairwise(code):
        seq1 += dists[kp1][c1][c2][1] + "A"
    seq2 = "A"
    for c1, c2 in pairwise(seq1):
        seq2 += dists[kp2][c1][c2][1] + "A"
    seq3 = ""
    for c1, c2 in pairwise(seq2):
        seq3 += dists[kp2][c1][c2][1] + "A"
    print(seq3)
    print(seq2[1:])
    print(seq1[1:])
    print(code[1:])
    print(f"{n=} {len(seq3)=}")
    part1 += n * len(seq3)


### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=21, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=21, year=2024)
