#!/usr/bin/env python3
from aoc_utils import ExecutionTime
from collections import defaultdict
from re import match, findall

def FindBagsRecursion(dict_of_rules: dict, target_bag: str="shiny gold") -> int:
    count = 0
    for rule in list(dict_of_rules):
        if any(target_bag in bag for bag in dict_of_rules[rule]) and not any('FLAGGED' in bag for bag in dict_of_rules[rule]):
            dict_of_rules[rule].append('FLAGGED')
            count += 1 + FindBagsRecursion(dict_of_rules, rule)
    
    return count        

def FindBagAmountRecursion(dict_of_rules: dict, target_bag: str="shiny gold") -> int:
    count = 0
    for bag in dict_of_rules[target_bag]:
        count += bag[0] * (1 + FindBagAmountRecursion(dict_of_rules, bag[1]))
    
    return count           

@ExecutionTime
def main():
    dict_of_rules = defaultdict(list)
    with open('./input.txt', 'r') as content:
        for line in content:
            outerbag = match(r'(.+?) bags contain', line)[1]
            for qty, innerbag in findall(r'(\d+) (.+?) bags?[,.]', line):
                qty = int(qty)
                dict_of_rules[outerbag].append((qty, innerbag))
    
    print(f"Puzzle 1 solution: {FindBagsRecursion(dict_of_rules)}\nPuzzle 2 solution: {FindBagAmountRecursion(dict_of_rules)}")

if __name__ == "__main__":                                          
    main()