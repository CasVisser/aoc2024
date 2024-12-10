import aocd, sys

inp = r"""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

if len(sys.argv) > 1 and (sys.argv[1] == "gd"):
    inp = aocd.get_data(day=7, year=2024)

part1 = part2 = 0

def possible(res, nums, part2=False):
    *nums, tl = nums
    q, r = divmod(res, tl)
    concat = str(res).endswith(str(tl))
    return res == tl or nums and (
            possible(res - tl, nums, part2=part2) or 
            r == 0 and possible(res // tl, nums, part2=part2) or
            part2 and concat and possible(res // 10**len(str(tl)), nums, part2=part2))

equations = [list(map(int, line.replace(":", "").split(" "))) for line in inp.split("\n")]
part1 = sum(res for res, *nums in equations if possible(res, nums))
part2 = sum(res for res, *nums in equations if possible(res, nums, part2=True))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
