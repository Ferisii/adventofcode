#!/usr/bin/env python3
from aoc_utils import ExecutionTime

def FindBagsRecursion(dict_of_rules: dict, target_bag: str="shiny gold") -> int:
    count = 0
    for rule in list(dict_of_rules):
        if any(target_bag in bag for bag in dict_of_rules[rule]) and not any("FLAGGED" in bag for bag in dict_of_rules[rule]):
            dict_of_rules[rule].append("FLAGGED")
            count += 1 + FindBagsRecursion(dict_of_rules, rule)
    
    return count        

def FindBagAmountRecursion(dict_of_rules: dict, target_bag: str="shiny gold") -> int:
    count = 0
    for bag in dict_of_rules[target_bag]:
        if bag != "no other":
            count += int(bag[0]) * (1 + FindBagAmountRecursion(dict_of_rules, bag[2:]))
    
    return count           

@ExecutionTime
def main():
    dict_of_rules = {}
    with open('./input.txt', 'r') as content:
        for line in content:
            outercolor, inner = line.strip().strip('.').split(' bags contain ')
            inner = inner.replace(' bags', '').replace(' bag', '').split(', ')
            dict_of_rules[outercolor] =  [column for column in inner]
    
    print(f"Puzzle 1 solution: {FindBagsRecursion(dict_of_rules)}\nPuzzle 2 solution: {FindBagAmountRecursion(dict_of_rules)}")

if __name__ == "__main__":                                          
    main()