import sys
input = sys.stdin.readline

N = int(input())
list = [0 for x in range(10000)]

for i in range(N):
    num = int(input())
    list[num-1] += 1

for i in range(len(list)):
    if list[i] == 0:
        continue
    else:
        for j in range(list[i]):
            print(i+1)
