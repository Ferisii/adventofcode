#!/usr/bin/env python3
from aoc_utils import ExecutionTime

def part1(list_of_lines: list):
    
    for index in range(len(list_of_lines)):
        for char in list_of_lines[index]:
            pass

def text2chart(text: str) -> dict:
    D = {}
    for index, row in enumerate(text.split()):
        for key, val in enumerate(row):
            D[complex(index, key)] = val
    return D

def changeseat(chart, seatkey):
    seat = chart[seatkey]
    if seat == '.':
        return seat
    occupied = 0
    for drxn in [-1, -1+1j, 1j, 1+1j, 1, 1-1j, -1j, -1-1j]:
        if chart.get(seatkey + drxn) == '#':
            occupied += 1
    if seat == 'L' and occupied == 0:
        return '#'
    if seat == '#' and occupied > 3:
        return 'L'
    return seat

def nextchart(chart):
    return {key: changeseat(chart, key) for key in chart}

def RunUnitllRepeat(chart):
    nc = nextchart(chart)
    while nc != chart:
        chart, nc = nc, nextchart(nc)
    return nc

def count_occupied(chart):
    return sum(v == "#" for v in chart.values())

def changeseat2(chart, seatkey):
    seat = chart[seatkey]
    if seat == '.':
        return seat
    occupied = 0
    for drxn in [-1, -1+1j, 1j, 1+1j, 1, 1-1j, -1j, -1-1j]:
        neighbor = '.'
        scale = 0
        while neighbor == '.':
            scale += 1
            neighbor = chart.get((scale * drxn) + seatkey)
        if neighbor == '#':
            occupied += 1
    if seat == 'L' and occupied == 0:
        return '#'
    if seat == '#' and occupied > 4:
        return 'L'
    return seat


def nextchart2(chart):
    return {key: changeseat2(chart, key) for key in chart}


def run_till_stabilized2(chart):
    nc = nextchart2(chart)
    while nc != chart:
        chart, nc = nc, nextchart2(nc)
    return nc


@ExecutionTime
def main():
    with open("./input.txt", "r") as content:
        #list_of_lines = [line.split() for line in content.readlines()]
        init_seats = content.read()
    
    initial_chart = text2chart(init_seats)
    stabilized = RunUnitllRepeat(initial_chart)
    part_1 = count_occupied(stabilized)
    
    print(part_1)
    
    stabilized2 = run_till_stabilized2(initial_chart)
    part_2 = count_occupied(stabilized2)
    print(part_2)
    
    

if __name__ == "__main__":
    main()