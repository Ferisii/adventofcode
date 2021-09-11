from aoc_utils import ExecutionTime


def s1(d):
    for k in range(25,len(d)):
        if not any(any(d[i] + d[j] == d[k] for j in range(i+1,k)) for i in range(k-25,k)):
            return k,d[k]


def s2(d,k,n):
    print(k, n)
    for i in range(0,k):
        for l in range(1,k-i):
            if (t := sum(d[i:i + l])) == n:
                return i, i+l
            if t>n:break

@ExecutionTime
def main():
    k, n = s1(d := list(map(int,open("input.txt","rt").read().split())))
    print(n)

    j, m = s2(d, k, n)
    print(min(d[j:m]) + max(d[j:m]))

if __name__ == "__main__":
    main()