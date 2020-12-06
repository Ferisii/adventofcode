#!/usr/bin/env python3
from aoc_utils import ExecutionTime

def AnswerCounter(list_of_lines: list):
    num1, num2 = 0, 0
    for line in list_of_lines:
        tmp_check1, tmp_check2, people = "", "", 1
        for char in line:
            if char == "\n":
                people += 1
            elif char not in tmp_check1:
                tmp_check1 += char
                num1 += 1
            else:
                tmp_check2 += char
        for char in "abcdefghijklmnopqrstuvwxyz":
            num2 += (tmp_check1 + tmp_check2).count(char) == people
    return num1, num2

@ExecutionTime
def main(): 
    with open("./input.txt", "r") as content:
        list_of_lines = list(([x.strip() for x in content.read().split("\n\n")]))
    
    puzzle1, puzzle2 = AnswerCounter(list_of_lines)
    
    print(f"Puzzle 1 solution: {puzzle1}\nPuzzle 2 solution: {puzzle2}")
    
if __name__ == "__main__":
    main()