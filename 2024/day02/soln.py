from lib.aoc import extract_input
import os


class Solution:

    def __init__(self) -> None:
        # sef.lines contains the input data from AOC
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        input_path = f"{dir_path[-1]}/input.txt"
        ex_input_path = f"{dir_path[-1]}/example.txt"
        if len(dir_path) > 1:
            input_path = f"{dir_path[-2]}/{dir_path[-1]}/input.txt"
            ex_input_path = f"{dir_path[-1]}/example.txt"
        self.lines = extract_input(input_path)
        self.ex_lines = extract_input(ex_input_path)

    def solve_part_1(self) -> None:
        safe = 0
        for s in self.lines:
            lvls = s.split(" ")
            lvls = [int(x) for x in lvls]
            # check if lvls are all decreasing or increasing
            if all(lvls[i] > lvls[i + 1] for i in range(len(lvls) - 1)) or all(
                lvls[i] < lvls[i + 1] for i in range(len(lvls) - 1)
            ):
                # iterate by pairs and check if adj pairs differ by at least 1 and at most 3
                arePairsValid = True
                for i in range(len(lvls) - 1):
                    lvl1, lvl2 = lvls[i], lvls[i + 1]
                    diff = abs(lvl2 - lvl1)
                    if diff > 3 or diff < 1:
                        arePairsValid = False
                        break
                if not arePairsValid:
                    continue
                safe += 1
        print(safe)
        pass

    def solve_part_2(self) -> None:
        safe = 0
        for s in self.lines:
            lvls = s.split(" ")
            lvls = [int(x) for x in lvls]
            for i in range(len(lvls)):
                new_lvls = [lvls[0:k] + lvls[k + 1 :] for k in range(len(lvls))]
                if self.is_safe(new_lvls[i]):
                    safe += 1
                    break

        print("safe pt 2", safe)
        pass

    def is_monotonic(self, lst: list):
        return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1)) or all(
            lst[i] < lst[i + 1] for i in range(len(lst) - 1)
        )

    def is_safe(self, lst: list):
        return self.is_monotonic(lst) and all(
            1 <= abs(lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1)
        )


s = Solution()
s.solve_part_1()
s.solve_part_2()
