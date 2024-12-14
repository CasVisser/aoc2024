import aocd, sys

inp = r"""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=14, year=2024)

### BEGIN SOLUTION

import re

w = 101; h = 103;
robots = [tuple(map(int, re.findall(r"-?\d+", line))) for line in inp.split("\n")]
for i in range(0, 10402):
    image = [["."] * w for _ in range(h)]
    for j, (x, y, dx, dy) in enumerate(robots): 
        robots[j] = ((x + dx) % w, (y + dy) % h, dx, dy)
        image[y][x] = "*"
    if i == 99:
        part1 = (len([r for r in robots if r[0] < w // 2 and r[1] < h // 2]) *
                 len([r for r in robots if r[0] > w // 2 and r[1] < h // 2]) *
                 len([r for r in robots if r[0] > w // 2 and r[1] > h // 2]) *
                 len([r for r in robots if r[0] < w // 2 and r[1] > h // 2]))
    if any("***********" in "".join(line) for line in image):
        print("\n".join("".join(line) for line in image))
        part2 = i
        break

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=14, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=14, year=2024)
