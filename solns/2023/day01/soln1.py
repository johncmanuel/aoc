
def get_lines(filename: str = "input.txt") -> list[str]:
    with open(filename) as f:
        return [line.rstrip() for line in f]
        
lines = get_lines()
total = 0

for i in range(len(lines)):
    l = lines[i]
    l = "".join(filter(str.isdigit, l))
    num = l[0] + l[-1]
    total += int(num)
    
print("Result:", total)