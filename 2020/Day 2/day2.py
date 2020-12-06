#!/usr/bin/env python3
from aoc_utils import ExecutionTime

def CharCountOrPosChecker(line: str, mode: str="c") -> bool:
    numbers, char, string = line.replace(":","").split(" ")
    num1, num2 = map(int, numbers.split("-"))
    if mode == "c":
        return num1 <= string.count(char) <= num2
    elif mode == "p":
        return (string[num1 - 1] == char) + (string[num2 - 1] == char) == 1
    raise Exception(f"'{mode}' is a non-valid mode. Valid modes are: 'c' count, or 'p' position.")

@ExecutionTime
def main():
    with open("./input.txt", "r") as content:
        lines = [x.strip() for x in content.readlines()]
    
    puzzle1, puzzle2 = 0, 0
    for line in lines:
        puzzle1 += CharCountOrPosChecker(line)
        puzzle2 += CharCountOrPosChecker(line, "p")
    print(f"Results for puzzle 1: {puzzle1}\nResults for puzzle 2: {puzzle2}")

if __name__ == "__main__":
    main()
    