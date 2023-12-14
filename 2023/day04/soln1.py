from lib.aoc import extract_input
import os

class Solution:

    def __init__(self) -> None:
        # get path of input file
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        self.lines = extract_input(f"./{dir_path[-2]}/{dir_path[-1]}/input.txt")

    def solve(self) -> None:
        count = 0
        for line in self.lines:
            line = line.split("|")
            win_nums = list(filter(len, line[0].split(":")[1].split(" ")))
            my_nums = list(filter(len, line[1].split(" ")))
            is_matched = False
            modifier = 0
            for n in my_nums:
                if n in win_nums:
                    is_matched = True
                    if is_matched:
                        if modifier == 0: modifier = 1
                        else: modifier *= 2
            count += modifier
        print(count)

s = Solution()
s.solve()