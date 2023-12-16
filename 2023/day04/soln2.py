from lib.aoc import extract_input
import os

class Solution:

    def __init__(self) -> None:
        # get path of input file
        dir_path = os.path.dirname(os.path.realpath(__file__)).split("\\")
        self.lines = extract_input(f"./{dir_path[-2]}/{dir_path[-1]}/input.txt")

    def solve(self) -> None:
        count = 0
        copies: dict[str, list[str]] = {}

        for c, cc in enumerate(self.lines):
            k = c+1
            if k not in copies: copies[k] = [cc]
            else: copies[k].append(cc)

        for card_num, card in enumerate(self.lines, 1):
            c = card.split("|")
            win_nums = list(filter(len, c[0].split(":")[1].split(" ")))
            my_nums = list(filter(len, c[1].split(" ")))
            matching_nums = 0
            
            for n in my_nums:
                if n in win_nums: matching_nums += 1
                    
            if matching_nums > 0:
                counter = 0
                # want to copy cards based on num of copies off current card
                while counter < len(copies[card_num]):
                    # copy cards starting from current card to the card based on # of matching nums
                    for i in range(card_num, card_num+matching_nums):
                        copies[i+1].append(self.lines[i])
                    counter += 1
        
        for k, v in copies.items():
            count += len(v)
            
        print(count)

s = Solution()
s.solve()