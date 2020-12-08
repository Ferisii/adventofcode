#!/usr/bin/env python3
from aoc_utils import ExecutionTime
from copy import deepcopy # Copies ALL the content within a list

@ExecutionTime
def RunUntilEndIsFound(list_of_lines: list, change: tuple=("jmp","nop")) -> int:
    range_of_list = range(len(list_of_lines))
    for tmp_index in range_of_list:
        tmp_lines = deepcopy(list_of_lines)
        if tmp_lines[tmp_index][0] == change[0]:
            tmp_lines[tmp_index][0] = change[1]
        else:
            continue

        accumulation, index = 0, 0
        index_set = set()
        
        while index not in index_set and index in range_of_list:
            index_set.add(index)
            if tmp_lines[index][0] == "acc":
                accumulation += int(tmp_lines[index][1])
                index += 1
            elif tmp_lines[index][0] == "nop":
                index += 1
            elif tmp_lines[index][0] == "jmp":
                index += int(tmp_lines[index][1])

        if index == len(tmp_lines):
            print(f"index_set={index_set}")
            return accumulation
    
    return 0 # Unlikely the result ever is 0... right?

def RunUntilRepeat(list_of_lines: list) -> int:
    range_of_list = range(len(list_of_lines))
    accumulation, index = 0, 0
    index_set = set()
    while index not in index_set and index in range_of_list:
        index_set.add(index)
        if list_of_lines[index][0] == "nop":
            index += 1
        elif list_of_lines[index][0] == "acc":
            accumulation += int(list_of_lines[index][1])
            index += 1
        elif list_of_lines[index][0] == "jmp":
            index += int(list_of_lines[index][1])

    return accumulation

@ExecutionTime
def main():
    with open("./input.txt") as content:
        list_of_lines = [line.strip().split(" ") for line in content]
    
    puzzle1 = RunUntilRepeat(list_of_lines)
    puzzle2 = RunUntilEndIsFound(list_of_lines)

    print(f"Puzzle 1 solution {puzzle1}\nPuzzle 2 solution: {puzzle2}")

if __name__ == "__main__":                                          
    main()