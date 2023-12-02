from lib.aoc import extract_input
import os

class Solution:

    def __init__(self) -> None:
        # get path of input file
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        self.lines = extract_input(f"./{dir_path[-2]}/{dir_path[-1]}/input.txt")

    def solve(self) -> None:
        # do something with input
        # ...
        print(self.lines)

s = Solution()
s.solve()