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
        self.skibidi = [list(line) for line in self.lines]
        self.guard_directions = {"^": (0, 1), "v": (0, -1), "<": (-1, 0), ">": (1, 0)}
        self.right_turns = {
            "^": ">",
            ">": "v",
            "v": "<",
            "<": "^",
        }

    def solve_part_1(self) -> None:
        obstacles = set()
        guard_pos = (0, 0)
        curr_dir_char = None

        for i in range(len(self.skibidi)):
            for j in range(len(self.skibidi[i])):
                if self.skibidi[i][j] == "#":
                    obstacles.add((i, j))
                if self.skibidi[i][j] in self.guard_directions.keys():
                    guard_pos = self.guard_directions[self.skibidi[i][j]]
                    curr_dir_char = self.skibidi[i][j]

        if not curr_dir_char:
            print("what the sigma this is so skibidi")
            return

        # begin the guard running in skibidi
        def move_guard(pos, direction):
            return (pos[0] + direction[0], pos[1] + direction[1])

        while 0 < guard_pos[0] < len(self.skibidi) and 0 < guard_pos[1] < len(
            self.skibidi[0]
        ):
            # check up, down, left, and right of guard pos
            guard_dirs = []
            for direction in self.guard_directions.values():
                guard_dir = move_guard(guard_pos, direction)
                if guard_dir in obstacles:
                    # turn right 90 degs
                    curr_dir_char = self.right_turns[curr_dir_char]

                guard_dirs.append(guard_dir)

    def solve_part_2(self) -> None:
        pass


s = Solution()
s.solve_part_1()
s.solve_part_2()
