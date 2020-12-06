#!/usr/bin/env python3
from aoc_utils import ExecutionTime
from itertools import combinations
from math import prod

def FindCombo(num_list: list, target: int, combo: int=2) -> tuple:
    for combo in combinations(num_list, combo):
        if sum(combo) == target:
            return combo
    raise Exception(f"Found no combo solution!")

@ExecutionTime
def main():
    with open("./input.txt", "r") as content:
        num_list = list(map(int, (x.strip() for x in content.readlines())))
    
    puzzle1 = prod(FindCombo(num_list, 2020))
    puzzle2 = prod(FindCombo(num_list, 2020, 3))
    
    print(f"Puzzle 1 solution: {puzzle1}\nPuzzle 2 solution: {puzzle2}")
    

if __name__ == "__main__":
    main()
    