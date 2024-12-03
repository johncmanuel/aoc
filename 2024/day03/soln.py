from lib.aoc import extract_input
import os
import re


class Solution:

    def __init__(self) -> None:
        # sef.lines contains the input data from AOC
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        input_path = f"{dir_path[-1]}/input.txt"
        if len(dir_path) > 1:
            input_path = f"{dir_path[-2]}/{dir_path[-1]}/input.txt"
        self.lines = extract_input(input_path)

    def solve_part_1(self) -> None:
        r = r"mul\((-?\d+),(-?\d+)\)"
        s = 0
        for k in self.lines:
            matches = re.findall(r, k)
            for m in matches:
                s += int(m[0]) * int(m[1])
        print(s)
        pass

    def solve_part_2(self) -> None:
        r = r"(mul\((-?\d+),(-?\d+)\)|do\(\)|don\'t\(\))"
        s = 0
        canDo = True
        for k in self.lines:
            matches = re.findall(r, k)
            for i in range(len(matches)):
                m = matches[i]
                if m[0] == "do()":
                    canDo = True
                elif m[0] == "don't()":
                    canDo = False
                if canDo and m[0].startswith("mul"):
                    s += int(m[1]) * int(m[2])
        print(s)
        pass


s = Solution()
s.solve_part_1()
s.solve_part_2()
