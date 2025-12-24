from pathlib import Path
from lib.aoc import extract_input


class Solution:
    def __init__(self) -> None:
        # Auto-detect year and day from folder structure: solns/YYYY/dayDD/soln.py
        path = Path(__file__)
        self.year = int(path.parent.parent.name)
        self.day = int(path.parent.name.replace("day", ""))

        self.lines = extract_input(self.year, self.day)

        self.password = 0
        self.curr_rotation = 50

    def rotate_left(self, rotations: int):
        # don't deal with negative numbers
        return self.rotate_right(100 - rotations)

    def rotate_right(self, rotations: int):
        total = self.curr_rotation + rotations
        return total % 100

    def solve_part_1(self) -> None:
        print("curr_rotation", self.curr_rotation)
        for instr in self.lines:
            direction, rotations = instr[0], int(instr[1::])
            if direction == "L":
                self.curr_rotation = self.rotate_left(rotations)
            elif direction == "R":
                self.curr_rotation = self.rotate_right(rotations)
            print(
                "curr_rotation:",
                self.curr_rotation,
                "direction:",
                direction,
                "rotation",
                rotations,
            )
            if self.curr_rotation == 0:
                self.password += 1
        print(self.password)

    def solve_part_2(self) -> None:
        pass


s = Solution()
s.solve_part_1()
s.solve_part_2()

