from lib.aoc import extract_input
import os


class Solution:

    def __init__(self) -> None:
        # sef.lines contains the input data from AOC
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        input_path = f"{dir_path[-1]}/input.txt"
        if len(dir_path) > 1:
            input_path = f"{dir_path[-2]}/{dir_path[-1]}/input.txt"
        self.lines = extract_input(input_path)

    def solve_part_1(self) -> None:
        pivot = self.lines.index("")
        rules, pages = self.lines[:pivot], self.lines[pivot + 1 :]
        rules_d = {}  # key: rule, value: set()
        middle_page_nums = 0
        for r in rules:
            k = r.split("|")
            x, y = int(k[0]), int(k[1])
            if x in rules_d:
                rules_d[x].add(y)
            else:
                rules_d[x] = set([y])
        # print(rules_d)
        for p in pages:
            page = [int(x) for x in p.split(",")]
            # go through each num and check ordering
            isCorrect = True
            for i, curr in enumerate(page):
                before, after = page[0:i], page[i + 1 :]
                if any(b in rules_d[curr] for b in before if curr in rules_d) or any(
                    x not in rules_d[curr] for x in after if curr in rules_d
                ):
                    isCorrect = False
                    break
            if not isCorrect:
                continue
            m = len(page) // 2
            middle_page_nums += page[m]
        print(middle_page_nums)

    def solve_part_2(self) -> None:
        pass


s = Solution()
s.solve_part_1()
s.solve_part_2()
