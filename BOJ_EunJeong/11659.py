import sys

input = sys.stdin.readline

N,M = map(int,input().split())
number = list(map(int,input().split()))
_sum = 0
_sumlist = [0,]

for i in number:
    _sum += i
    _sumlist.append(_sum)

for _ in range(M):
    i,j = map(int,input().split())
    print(_sumlist[j] - _sumlist[i-1])
