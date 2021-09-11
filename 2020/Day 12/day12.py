#!/usr/bin/env python3
from aoc_utils import ExecutionTime

def InstructExecutor(line_list: list) -> int:
    x, y, f = 0, 0, 90
    for line in line_list:
        command, value = line[:1], int(line[1:])
        if command == "N":
            y += value
        elif command == "S":
            y -= value
        elif command == "E":
            x += value
        elif command == "W":
            x -= value
        elif command == "R":
            f += value
        elif command == "L":
            f -= value
        elif command == "F": # 0 = north, 1 = east, 2 = south, 3 = west
            if (direction := f / 90 % 4) == 0:
                y += value
            elif direction == 1:
                x += value
            elif direction == 2:
                y -= value
            elif direction == 3:
                x -= value
    return abs(x) + abs(y)

def WaypointExecutor(line_list: list) -> int:
    x, y = 0, 0
    wx, wy = 10, 1
    for line in line_list:
        command, value = line[:1], int(line[1:])
        if command == 'F':
            x += wx * value
            y += wy * value
        elif command == 'N':
            wy += value
        elif command == 'E':
            wx += value
        elif command == 'S':
            wy -= value
        elif command == 'W':
            wx -= value
        elif command == 'L':
            while value:
                wx, wy = -wy, wx
                value -= 90
        elif command == 'R':
            while value:
                wx, wy = wy, -wx
                value -= 90
    
    return abs(x) + abs(y)

@ExecutionTime
def main():
    with open("./input.txt", "r") as content:
        line_list = [x.strip() for x in content.readlines()]
    
    puzzle1 = InstructExecutor(line_list)
    puzzle2 = WaypointExecutor(line_list)
    
    print(f"Puzzle 1 result: {puzzle1}\nPuzzle 2 result: {puzzle2}")

if __name__ == "__main__":
    main()