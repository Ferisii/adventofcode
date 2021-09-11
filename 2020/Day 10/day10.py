#!/usr/bin/env python3
from aoc_utils import ExecutionTime
from math import prod

def PartialSumAlgorithm(num_list: list, target_value: int=1) -> list:
    list_a = list() # Append difference between index1 and index2 to list
    for index in range(len(num_list) - 1): 
        list_a.append(num_list[index + 1] - num_list[index])
    
    list_b = list() # Group together adjacent 1's and append sum of them to list
    tmp_value = 0
    for index in range(len(list_a)):
        if (value := list_a[index]) == target_value:
            tmp_value += value
        elif tmp_value > target_value:
            list_b.append(tmp_value)
        tmp_value = tmp_value if value == target_value else 0
    
    list_c = list() # Find partial sum of each value
    for index in range(len(list_b)): 
        n = list_b[index]
        list_c.append(int((n ** 2 - n) / 2 + 1))
        
    return list_c

def IntWidthOccurrences(num_list: list, width1: int=1, width2: int=3) -> tuple:
    a, b = 0, 0
    for index in range(len(num_list) - 1):
        if (tmp_value :=num_list[index+1] - num_list[index]) == width1:
            a += 1
        elif tmp_value == width2:
            b += 1
    
    return a, b

@ExecutionTime
def main():
    with open("./input.txt", "r") as content:
        num_list = list(map(int, (x.strip() for x in content.readlines())))
        # Adding 0 and max(adapter) + 3 to the list, then sort it
        num_list.append(0)
        num_list.append(max(num_list)+3) 
        num_list = sorted(num_list)
    
    puzzle1 = IntWidthOccurrences(num_list)
    puzzle2 = PartialSumAlgorithm(num_list)
    
    print(f"Puzzle 1 solution: {prod(puzzle1)}\nPuzzle 2 solution: {prod(puzzle2)}")
 
if __name__ == "__main__":
    main()