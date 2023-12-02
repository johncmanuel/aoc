import re

def extract_input(filename: str = "input.txt") -> list[str]:
    with open(filename) as f:
        return [line.rstrip() for line in f]

lines = extract_input()

rgb_limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0

for i in range(len(lines)):
    l = lines[i].split(";")
    exceedLimit = False
    for x in l:
        cubes: list[str] = re.findall("\d+ green|\d+ blue|\d+ red", x)
        for cube in cubes:
            color, num = next((c for c in rgb_limits.keys() if c in cube)), int(re.search("\d+", cube)[0])
            if num > rgb_limits[color]:
                exceedLimit = True
                break
    if not exceedLimit: total += (i+1)
print(total)