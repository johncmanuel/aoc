from lib.aoc import extract_input
import os
from collections import Counter


class Solution:

    def __init__(self) -> None:
        # sef.lines contains the input data from AOC
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        input_path = f"{dir_path[-1]}/input.txt"
        if len(dir_path) > 1:
            input_path = f"{dir_path[-2]}/{dir_path[-1]}/input.txt"
        self.lines = extract_input(input_path)

    def solve_part_1(self) -> None:
        distance = 0
        left = []
        right = []
        for s in self.lines:
            y = s.split("  ")
            left.append(int(y[0]))
            right.append(int(y[1]))
        while len(left) > 0 and len(right) > 0:
            minLeft, minRight = min(left), min(right)
            distance += abs(minLeft - minRight)
            left.remove(minLeft)
            right.remove(minRight)
        print(distance)

    def solve_part_2(self) -> None:
        left = []
        right = []
        for s in self.lines:
            y = s.split("  ")
            left.append(int(y[0]))
            right.append(int(y[1]))
        right = Counter(right)
        similarity = 0
        for num in left:
            if num in right:
                similarity += right[num] * num
        print(similarity)


s = Solution()
s.solve_part_1()
s.solve_part_2()
