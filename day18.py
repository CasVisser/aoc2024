import aocd, sys

inp = r"""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=18, year=2024)

### BEGIN SOLUTION

from collections import defaultdict
from heapq import heappush, heappop

size = 71

lines = inp.split("\n")
grid = {complex(x, y) for x in range(size) for y in range(size)}
goal = complex(size - 1, size - 1)
lo = 0; mid = 1024; hi = inp.count("\n")
while lo < hi:
    corrupted = {complex(line.replace(",", "+") + "j") for line in lines[:mid]}
    dist = defaultdict(lambda: size * size + 1)
    dist[0] = 0
    q = [(0, counter := 0, 0)]
    while q:
        cur_dist, _, pos = heappop(q)
        if pos == goal:
            break
        for n in [pos + d for d in [1, -1j, -1, 1j] if pos + d in grid and pos + d not in corrupted]:
            if cur_dist + 1 < dist[n]:
                dist[n] = cur_dist + 1
                heappush(q, (cur_dist + 1, counter := counter + 1, n))
    if mid == 1024:
        part1 = dist[goal]
    if dist[goal] < size * size + 1:
        lo = mid + 1
    else:
        hi = mid - 1
    mid = lo + ((hi - lo) // 2)

part2 = lines[mid]

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=18, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=18, year=2024)
