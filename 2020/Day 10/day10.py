#!/usr/bin/env python3


def main():
    with open("./input.txt", "r") as content:
        num_list = list(map(int, (x.strip() for x in content.readlines())))
    
    num_list = sorted(num_list)
    results = [1, 0, 1]
    for index in range(len(num_list)):
        tmp_value = num_list[index]
        if tmp_value + 1 in num_list:
            results[0] += 1
            continue
        elif tmp_value + 2 in num_list:
            results[1] += 1
            continue
        elif tmp_value + 3 in num_list:
            results[2] += 1
        else:
            break
    print(num_list)
    print(results)
    print(results[0] * results[2])

    """while True:
        popped = num_list.pop(0)
        if num_list[0] == popped + 1:
            results[0] += 1
        elif num_list[0] == popped + 2:
            results[1] += 1
        elif num_list[0] == popped + 3:
            results[2] += 1
        else:
            break
    print(results)"""


if __name__ == "__main__":
    main()