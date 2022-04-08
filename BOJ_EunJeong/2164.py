import sys
input = sys.stdin.readline

N = int(input())
num = 1

while True:
    if N == num:
        print(N)
        break
    elif N-num < num:
        print(2*(N-num))
        break
    else:
        num = num*2
