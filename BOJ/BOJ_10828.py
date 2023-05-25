import sys


def push(l, x):
    l.append(x)


def empty(l):
    if (len(l) == 0):
        return 1
    else:
        return 0


def pop(l):
    if (empty(l) == 1):
        return -1
    else:
        return l.pop()


def size(l):
    return len(l)


def top(l):
    if (empty(l) == 1):
        return -1
    else:
        return l[len(l) - 1]


if __name__ == "__main__":
    n = int(input())
    stack = []
    for x in range(n):
        # n=list(map(str,input().split()))
        n = list(map(str, sys.stdin.readline().split()))
        if (len(n) > 1):
            push(stack, int(n[1]))
        else:
            if (n[0] == "pop"):
                print(pop(stack))
            elif (n[0] == "size"):
                print(size(stack))
            elif (n[0] == "empty"):
                print(empty(stack))
            else:
                print(top(stack))
