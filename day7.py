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

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=7, year=2024)

### BEGIN SOLUTION

def get_possible_results(nums):
    if len(nums) == 1:
        return {nums[0]}
    rec = get_possible_results(nums[:-1])
    return {nums[-1] + r for r in rec} | {nums[-1] * r for r in rec} | {int(str(r) + str(nums[-1])) for r in rec}

part1 = part2 = 0
for line in inp.split("\n"):
    r, nums = line.split(": ")
    nums = list(map(int, nums.split(" ")))
    rs = get_possible_results(nums)
    print(rs)
    if int(r) in rs:
        part2 += int(r)


### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=7, year=2024)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=7, year=2024)
