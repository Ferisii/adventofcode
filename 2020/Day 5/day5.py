#!/usr/bin/env python3

def SeatString2Bin(string: str, keynvalues: dict=None, bintype: int=2) -> int:
    if keynvalues != None:
        string = string.translate(str.maketrans(keynvalues))
    return int(string, bintype)

def main():
    with open("./input.txt", "r") as content:
        lines = [x.strip() for x in content.readlines()]
    
    puzzle_input = []
    keynvalues = {"F":"0","B":"1","L":"0","R":"1"}
    for line in lines:
        puzzle_input.append(SeatString2Bin(line, keynvalues))
    
    for seat in puzzle_input:
        # Seat has to be between min. and max. values from the list
        if seat + 1 not in puzzle_input and seat + 2 in puzzle_input:
            puzzle2 = seat + 1
            break
    
    print(f"Puzzle 1 solution: {max(puzzle_input)}\nPuzzle 2 solution: {puzzle2}")

if __name__ == "__main__":
    from time import time
    start_time = time()
    main()
    print(f"Solved in {round(time() - start_time, 4)} seconds.")