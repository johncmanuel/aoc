def get_lines(filename: str = "input.txt") -> list[str]:
    with open(filename) as f:
        return [line.rstrip() for line in f]
    
lines = get_lines()
total = 0

d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for i in range(len(lines)):
    l, l_r = lines[i], lines[i][::-1]
    front_str = back_str = ""
    for ch in l:
        if any(x in front_str for x in d):
            front_str = str(d[next((x for x in d if x in front_str), False)])
            break
        elif ch.isdigit():
            front_str = str(ch)
            break
        front_str += ch
    for ch_r in l_r:
        if any(x in back_str[::-1] for x in d):
            back_str = str(d[next((x for x in d if x in back_str[::-1]), False)])
            break
        elif ch_r.isdigit():
            back_str = str(ch_r)
            break
        back_str += ch_r
    print(front_str, back_str)
    n = front_str + back_str
    total += int(n)

print("Result:", total)