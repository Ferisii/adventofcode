#!/usr/bin/env python3
from aoc_utils import ExecutionTime
from math import prod

def CharCheckerSloper(string_list: list, x_incr: int, y_incr: int, char: str="#") -> int:
    x, y, result = 0, 0, 0
    list_length = len(string_list)
    string_length = len(string_list[0]) # We presume every string has the same length
    
    while y < list_length:
        result += char == string_list[y][x % string_length]
        x += x_incr
        y += y_incr
    
    return result

@ExecutionTime
def main():
    puzzles = [(3,1), (1,1), (5,1), (7,1), (1,2)]
    results = []
    
    with open("./input.txt", "r") as content:
        string_list = [x.strip() for x in content.readlines()]
    
    for x, y in puzzles:
        results.append(CharCheckerSloper(string_list, x, y))
    
    print(f"Puzzle 1 result: {results[0]}\nPuzzle 2 result: {prod(results)}")
        

if __name__ == "__main__":
    main()