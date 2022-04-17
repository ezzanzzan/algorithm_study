import sys
input = sys.stdin.readline

N = int(input())
list = []

for i in range(N):
    [x,y] = map(int,input().split())
    list.append([x,y])

list.sort(key = lambda x:(x[0],x[1]))

for i in range(len(list)):
    print(list[i][0],list[i][1])
