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

part1 = part2 = 0

def combo(op, A, B, C):
    if op < 4:
        return op
    return [A, B, C][op - 4]

A, B, C, *prog = map(int, re.findall(r"\d+", inp))
s = 20534812061143
for start_A in range(s * 8, (s + 1) * 8):
    A = start_A
    out = []
    pc = 0
    while pc < len(prog) - 1:
        ins, op = prog[pc : pc + 2]
        if ins == 0: # adv
            A = A // 2**(combo(op, A, B, C))
        elif ins == 1: # blx
            B ^= op
        elif ins == 2: # bst
            B = combo(op, A, B, C) & 7
        elif ins == 3 and A != 0: # jnz
            pc = op
            continue
        elif ins == 4: # bxc
            B = B ^ C
        elif ins == 5: # out
            out.append(combo(op, A, B, C) & 7)
        elif ins == 6: # bdv
            B = A // 2**(combo(op, A, B, C))
        elif ins == 7: # cdv
            C = A // 2**(combo(op, A, B, C))
        pc += 2
    print(f"{start_A}: {','.join(map(str, out))}")
    if out == prog:
        part2 = start_A

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=17, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=17, year=2024)
