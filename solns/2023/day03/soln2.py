from lib.aoc import extract_input
import os

class Solution:

    def __init__(self) -> None:
        # get path of input file and extract it
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        self.lines = extract_input(f"./{dir_path[-2]}/{dir_path[-1]}/input.txt")

    def solve(self) -> None:
        # top:      [row-1][col]
        # bot:      [row+1][col]
        # left:     [row][col-1]
        # right:    [row][col+1]
        # diagonal: [row+1][col+1], [row+1][col-1], [row-1][col+1], [row-1][col-1]
        DIRECTIONS = (
            (-1, 0), 
            (1, 0), 
            (0, -1), 
            (0, 1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        )
        count = 0

        def get_adj_nums_pos(lines: list[str], row: int, col: int) -> list[tuple[int, int]]:
            nums_pos = []
            for dir_r, dir_c in DIRECTIONS:
                n_row, n_col = row + dir_r, col + dir_c
                if 0 <= n_row < len(lines) and 0 <= n_col < len(lines[0]):
                    n = lines[n_row][n_col]
                    if n.isdigit():
                        nums_pos.append((n_row, n_col))
            return nums_pos
        
        def partition_list(l: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
            p = []
            curr_p = [l[0]]
            for i in range(1, len(l)):
                curr = l[i]
                prev = l[i - 1]
                if curr[1] - prev[1] == 1:
                    curr_p.append(curr)
                else:
                    p.append(curr_p)
                    curr_p = [curr]
            p.append(curr_p)
            return p
        
        def contains_adj_num(adj_num_pos: tuple, num_pos: tuple):
            return bool(set(adj_num_pos) & set(num_pos))

        d: dict[str, list[tuple[int, int]]] = {}
        stars = {}
        nums_pos: list[tuple[int, int]] = []
        nums = {}
        for i, l in enumerate(self.lines):
            for j, c in enumerate(l):
                if c == "*":
                    if c not in d:
                        d[c] = [(i, j)]
                    else:
                        d[c].append((i, j))
                # get nums and their pos
                elif c.isdigit():
                    nums_pos.append((i, j))
        
        for star in d["*"]:
            row, col = star
            adj_nums_pos = get_adj_nums_pos(self.lines, row, col)
            if (row, col) not in stars and len(adj_nums_pos) >= 2:
                stars[(row, col)] = adj_nums_pos

        for p in partition_list(nums_pos):
            nums[tuple(p)] = "".join(self.lines[r][c] for r, c in p)

        # get nums adjacent to star
        adj_nums = {}
        for star_coords, adj_nums_coords in stars.items():
            for num_coords, num in nums.items():
                if contains_adj_num(tuple(adj_nums_coords), num_coords):
                    if star_coords not in adj_nums:
                        adj_nums[star_coords] = [num]
                    else:
                        adj_nums[star_coords].append(num)

        for p, pp in adj_nums.items(): 
            if len(pp) == 2:
                count += (int(pp[0]) * int(pp[1]))

        print(count)

s = Solution()
s.solve()