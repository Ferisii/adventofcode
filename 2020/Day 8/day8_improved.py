from aoc_utils import ExecutionTime

def TheReturner(list_of_lines: list, index: int=0, acc: int=0):
    if list_of_lines[index][0] == "acc":
        acc += list_of_lines[index][1]
        index += 1
    elif list_of_lines[index][0] == "nop":
        index += 1
    elif list_of_lines[index][0] == "jmp":
        index += list_of_lines[index][1] if list_of_lines[index][1] != 0 else 1
    
    return index, acc

def ComputeList(list_of_lines: list, pathfinder: tuple=None) -> int:
    list_range = range(len(list_of_lines))
    index, acc = 0, 0
    index_set = set()
    if pathfinder == None:
        while index not in index_set and index in list_range:
            index_set.add(index)
            index, acc = TheReturner(list_of_lines, index, acc)
    else:
        for tmp_operator in pathfinder:
            ori_operator = pathfinder[0] if tmp_operator == pathfinder[1] else pathfinder[1]
            for tmp_index in list_range:
                if list_of_lines[tmp_index][0] in (tmp_operator, "acc"):
                    continue
                list_of_lines[tmp_index][0] = tmp_operator
                while index not in index_set and index in list_range:
                    index_set.add(index)
                    index, acc = TheReturner(list_of_lines, index, acc)
                    if index in index_set: # Repeat found? reset
                        list_of_lines[tmp_index][0] = ori_operator
                        index, acc = 0, 0
                        index_set = set()
                        break
                    elif index == list_range[-1]:
                        return acc
        return None   
    return acc

@ExecutionTime
def main():
    with open("input.txt", "r") as content:
        list_of_lines = [[operator, int(increment)] for operator, increment in [line.strip().split() for line in content.readlines()]]
    
    puzzle1 = ComputeList(list_of_lines)
    puzzle2 = ComputeList(list_of_lines, ("nop", "jmp"))
    
    print(f"Puzzle 1 solution: {puzzle1}\nPuzzle 2 solution: {puzzle2}")

if __name__ == "__main__":
    main()