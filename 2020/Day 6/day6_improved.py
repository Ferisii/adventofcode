#!/usr/bin/env python3

def AnswerCounter(list_of_lines: list) -> tuple:
    num1, num2 = 0, 0
    for line in list_of_lines:
        num1 += len(set(line.replace("\n","")))
        num2 += len(set.intersection(*map(set, line.split("\n"))))
    return num1, num2
    

def main(): 
    with open("./input.txt", "r") as content:
        list_of_lines = list(([x.strip() for x in content.read().split("\n\n")]))
    
    puzzle1, puzzle2 = AnswerCounter(list_of_lines)

    print(f"Puzzle 1 solution: {puzzle1}\nPuzzle 2 solution: {puzzle2}")
    
if __name__ == "__main__":
    from time import time
    start_time = time()
    main()
    print(f"\nSolved in {round(time() - start_time, 4)} seconds.")