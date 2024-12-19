import aocd, sys

inp = r"""Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=17, year=2024)

### BEGIN SOLUTION

import re

A, B, C, *prog = map(int, re.findall(r"\d+", inp))
candidates = [A] + list(range(8))
part1 = part2 = 0
while candidates:
    part2 = A = candidates.pop(0)
    out = []
    pc = 0
    while pc < len(prog) - 1:
        ins, op = prog[pc : pc + 2]
        combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}[op]
        match ins:
            case 0: A = A >> combo        # adv
            case 1: B ^= op               # blx
            case 2: B = combo & 7         # bst
            case 3:                       # jnz
                if A != 0:
                    pc = op
                    continue
            case 4: B = B ^ C             # bxc
            case 5: out.append(combo & 7) # out
            case 6: B = A >> combo        # bdv
            case 7: C = A >> combo        # cdv
        pc += 2
    if part1 == 0:
        part1 = ",".join(map(str, out))
    if out == prog:
        break
    if out == prog[-len(out):]:
        candidates = list(range(part2 * 8, (part2 + 1) * 8)) + candidates

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=17, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=17, year=2024)
