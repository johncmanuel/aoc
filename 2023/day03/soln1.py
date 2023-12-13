from lib.aoc import extract_input
import os

class Solution:

    def __init__(self) -> None:
        # get path of input file and extract it
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        self.lines = extract_input(f"./{dir_path[-2]}/{dir_path[-1]}/input.txt")

    def solve(self) -> None:
        # self.lines = [list(s.strip()) for s in self.lines]
        
        # top:      [row-1][col]
        # bot:      [row+1][col]
        # left:     [row][col-1]
        # right:    [row][col+1]
        # diagonal: [row+1][col+1], [row+1][col-1], [row-1][col+1], [row-1][col-1]
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1))
        count = 0

        def does_ch_contain_symbol(lines: list[str], ch_row: int, ch_col: int) -> bool:
            contains_symbol = False
            for dir_r, dir_c in DIRECTIONS:
                n_row, n_col = ch_row + dir_r, ch_col + dir_c
                # when checking neighbors out of bounds, assume there are no symbols
                if 0 <= n_row < len(lines) and 0 <= n_col < len(lines[0]):
                    n = lines[n_row][n_col]
                    if n.isdigit() or n == ".":
                        continue
                    contains_symbol = True
            return contains_symbol
       
        for line_idx, line in enumerate(self.lines):
            has_symbol = []
            number = ""
            for ch_idx, ch in enumerate(line):
                if ch.isdigit():
                    number += ch
                    s = does_ch_contain_symbol(self.lines, line_idx, ch_idx)
                    has_symbol.append(s)
                else:
                    if any(has_symbol):
                        count += int(number)
                    has_symbol = []
                    number = ""
            # Account for numbers on the rightmost edge (before entering new line)
            if number != "":
                if any(has_symbol):
                    count += int(number)
                has_symbol = []
                number = ""
        print(count)

s = Solution()
s.solve()