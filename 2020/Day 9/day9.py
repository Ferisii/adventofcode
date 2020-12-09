#!/usr/bin/env python3
from aoc_utils import ExecutionTime
from itertools import combinations

def FindInvalidCombo(num_list: list, target_value: int, min_combo: int=2, linear: bool=True) -> list:
    num_list = num_list[:num_list.index(target_value)] if linear else num_list
    for index1 in range(len(num_list)):
        for index2 in range(index1 + min_combo, len(num_list)):
            tmp_list = num_list[index1:index2]
            if sum(tmp_list) == target_value:
                return tmp_list

def FindInvalidInt(num_list: list, index_range: int=25) -> int:
    for index in range(index_range, len(num_list)):
        tmp_list = num_list[index - index_range:index]
        if not any([a + b == num_list[index] for a, b in combinations(tmp_list, 2)]):
            return num_list[index]

@ExecutionTime
def main():
    with open("./input.txt", "r") as content:
        num_list = list(map(int, (x.strip() for x in content.readlines())))
    
    puzzle1 = FindInvalidInt(num_list)
    puzzle2 = FindInvalidCombo(num_list, puzzle1)
    
    print(f"Puzzle 1 solution: {puzzle1}\nPuzzle 2 solution: {min(puzzle2) + max(puzzle2)}")

if __name__ == "__main__":
    main()