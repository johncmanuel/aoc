import re

def extract_input(filename: str = "input.txt") -> list[str]:
    with open(filename) as f:
        return [line.rstrip() for line in f]

lines = extract_input()

rgb = {
    "red": 1,
    "green": 1,
    "blue": 1
}

total = 0

for i in range(len(lines)):
    l = lines[i].split(";")
    for x in l:
        cubes: list[str] = re.findall("\d+ green|\d+ blue|\d+ red", x)
        for cube in cubes:
            color, num = next((c for c in rgb.keys() if c in cube)), int(re.search("\d+", cube)[0])
            rgb[color] = max(num, rgb[color])
    total += (rgb["red"] * rgb["green"] * rgb["blue"])
    rgb = rgb.fromkeys(rgb, 1)
print(total)