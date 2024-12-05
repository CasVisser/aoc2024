import aocd, sys

inp = r"""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=5, year=2024)

# Common parsing steps
lines = inp.split("\n")

# If multiple lines of same length, try to parse as grid
if len(lines) > 1 and len(set(map(len, lines))) == 1:
    grid = {complex(x, y): c for y, line in enumerate(lines)
                             for x, c in enumerate(line)}

part1 = None
part2 = None

### BEGIN SOLUTION

from collections import defaultdict

part1 = part2 = 0

g = defaultdict(list)

unordered = []
rules, pagess = inp.split("\n\n")
for rule in rules.split("\n"):
    n1, n2 = rule.split("|")
    g[n1].append(n2)

for pages in pagess.split("\n"):
    ps = pages.split(",")
    ordered = True
    for i, p1 in enumerate(ps):
        for p2 in ps[i + 1:]:
            if p1 in g[p2]:
                ordered = False
                unordered.append(ps)
                break
        if not ordered:
            break
    else:
        part1 += int(ps[len(ps) // 2])

import sys
sys.setrecursionlimit(10000000)
from collections import deque
for ps in unordered:
    seen = set()
    topological = deque()
    def visit(v):
        if v in seen:
            return
        for neighbor in g[v]:
            if neighbor not in ps:
                continue
            visit(neighbor)
        seen.add(v)
        topological.appendleft(v)

    for p in ps:
        if p in seen:
            continue
        visit(p)
    ps.sort(key=lambda p: topological.index(p))
    part2 += int(ps[len(ps) // 2])







### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=5, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=5, year=2024)
