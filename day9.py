import aocd, sys

inp = r"""112333133121414131402"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=9, year=2024)

### BEGIN SOLUTION

from collections import defaultdict

mem = []
empty_spaces = []
files = []
empty_ranges = []
for i, size in enumerate(map(int, inp)):
    if i % 2 == 0:
        files.append([len(mem), len(mem) + size, size, i // 2])
        mem += [i // 2] * size
    else:
        empty_ranges.append([len(mem), len(mem) + size, size])
        empty_spaces += list(range(len(mem), len(mem) + size))
        mem += ["."] * size

empty_i = 0
for i in range(len(mem) - 1, -1, -1):
    if mem[i] == ".":
        continue
    if empty_spaces[empty_i] >= i:
        break
    mem[empty_spaces[empty_i]] = mem[i]
    empty_i += 1
    mem[i] = "."

part1 = sum(f_id * i for f_id, i in zip(mem, range(len(mem))) if f_id != ".")

for file in reversed(files):
    f_start, f_end, f_size, f_id = file
    for empty_range in empty_ranges:
        e_start, e_end, e_size = empty_range
        if e_size < f_size:
            continue
        if e_start >= f_start:
            break
        file[0] = e_start
        file[1] = e_start + f_size
        empty_range[0] = file[1]
        empty_range[2] = e_end - empty_range[0]
        break
        
part2 = sum(f_id * i for f_start, f_end, f_size, f_id in files for i in range(f_start, f_end))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=9, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=9, year=2024)
