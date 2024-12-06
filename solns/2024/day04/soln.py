from lib.aoc import extract_input
import os


class Solution:

    def __init__(self) -> None:
        # sef.lines contains the input data from AOC
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        input_path = f"{dir_path[-1]}/ex.txt"
        if len(dir_path) > 1:
            input_path = f"{dir_path[-2]}/{dir_path[-1]}/ex.txt"
        self.lines = extract_input(input_path)

    def solve_part_1(self) -> None:
        word = "XMAS"
        word_reversed = word[::-1]
        matrix = [list(line) for line in self.lines]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        # visited = set()

        def dfs(i, j, next_word) -> bool:
            # if (i, j) in visited:
            #     return False
            # visited.add((i, j))
            for d in dirs:
                next_i, next_j = i + d[0], j + d[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[next_i][next_j] == next_word[0]:
                        if len(next_word) == 1:
                            return True
                        print(next_word, (next_i, next_j))
                        return dfs(next_i, next_j, next_word[1:])
            return False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == word[0]:
                    if dfs(i, j, word[1:]):
                        res += 1
                elif matrix[i][j] == word_reversed[0]:
                    if dfs(i, j, word_reversed[1:]):
                        res += 1

        print(res)

    def solve_part_2(self) -> None:
        pass


s = Solution()
s.solve_part_1()
s.solve_part_2()
