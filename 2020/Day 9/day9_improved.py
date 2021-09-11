#!/usr/bin/env python3
from aoc_utils import ExecutionTime

def FindInvalidCombo(num_list: list, value_target: int, index_target: int) -> list:
    for index1 in range(0, index_target):
        for index2 in range(1, index_target - index1):
            if (tmp_value := sum(num_list[index1:index1 + index2])) == value_target:
                return num_list[index1:index1 + index2]
            elif tmp_value > value_target:
                break

def FindInvalidInt(num_list: list, index_range: int=25) -> tuple:
    for index1 in range(index_range, len(num_list)):
        if not any(any(num_list[index3] + num_list[index2] == num_list[index1] for index2 in range(index3 + 1, index1)) for index3 in range(index1 - index_range, index1)):
            return num_list[index1], index1

@ExecutionTime
def main():
    with open("./input.txt", "r") as content:
        num_list = list(map(int, content.read().split()))
    
    puzzle1, index = FindInvalidInt(num_list)
    puzzle2 = FindInvalidCombo(num_list, puzzle1, index)
    
    print(f"Puzzle 1 solution: {puzzle1}\nPuzzle 2 solution: {min(puzzle2) + max(puzzle2)}")

if __name__ == "__main__":
    main()