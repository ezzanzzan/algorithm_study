import sys

input = sys.stdin.readline

N = input()
N = list(N)
N.sort(reverse=True)

for i in N:
    print(i, end="")
