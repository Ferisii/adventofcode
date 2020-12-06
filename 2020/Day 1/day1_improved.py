#!/usr/bin/env python3
from itertools import combinations
from math import prod

def FindCombo(num_list: list, target: int, combo: int=2) -> tuple:
    for combo in combinations(num_list, combo):
        if sum(combo) == target:
            return combo
    raise Exception(f"Found no combo solution!")

def main():
    with open("./numberlist.txt", "r") as content:
        num_list = list(map(int, (x.strip() for x in content.readlines())))
    
    puzzle1 = prod(FindCombo(num_list, 2020))
    puzzle2 = prod(FindCombo(num_list, 2020, 3))
    
    print(f"Puzzle 1 solution: {puzzle1}\nPuzzle 2 solution: {puzzle2}")
    

if __name__ == "__main__":
    from time import time
    start_time = time()
    main()
    print(f"Solved in {round(time() - start_time, 4)} seconds.")
    