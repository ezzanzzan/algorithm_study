import sys

input = sys.stdin.readline

N = int(input())
_list = list(map(int,input().split()))
_list2 = sorted(list(set(_list)))

dic = {_list2[i]: i for i in range(len(_list2))}

for i in _list:
    print(dic[i], end=' ')
