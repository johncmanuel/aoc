from pathlib import Path
from lib.aoc import extract_input


class Solution:
    def __init__(self) -> None:
        # Auto-detect year and day from folder structure: solns/YYYY/dayDD/soln.py
        path = Path(__file__)
        self.year = int(path.parent.parent.name)
        self.day = int(path.parent.name.replace("day", ""))

        self.lines = extract_input(self.year, self.day)

    def solve_part_1(self) -> None:
        print(self.lines)
        pass

    def solve_part_2(self) -> None:
        pass


s = Solution()
s.solve_part_1()
s.solve_part_2()

