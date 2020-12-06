#!/usr/bin/env python3
import time

start_time = time.time()
target = 2020
solutions = {"Assignment1": [],
             "Assignment2": []}

# Puzzle 1
with open("./numberlist.txt", "r") as content:
    content = content.readlines()
    for line_a in content:
        for line_b in content:
            a, b = int(line_a), int(line_b)
            if a + b == target:
                solution = set((a, b))
                if solution not in solutions["Assignment1"]:
                    solutions["Assignment1"].append(solution)
                    print(f"Found solution: '{a}' and '{b}' sums up to {target}!\nMultiplying them returns '{a * b}'!")

# Puzzle 2
with open("./numberlist.txt", "r") as content:
    content = content.readlines()
    for line_a in content:
        for line_b in content:
            for line_c in content:
                a, b, c = int(line_a), int(line_b), int(line_c)
                if a + b + c == target:
                    solution = set((a, b, c))
                    if solution not in solutions["Assignment2"]:
                        solutions["Assignment2"].append(solution) 
                        print(f"Found solution: '{a}', '{b}' and {c} sums up to {target}!\nMultiplying them returns '{a * b * c}'!")
print(solutions)
print(f"Solved in {time.time() - start_time}")