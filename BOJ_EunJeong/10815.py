import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int,input().split()))
M = int(input())
_list = list(map(int,input().split()))
card.sort()

for i in _list:
    start,end,check = 0,len(card)-1,0
    while start<=end:
        mid = (start+end)//2
        if card[mid] == i:
            check = 1
            break
        elif card[mid] < i:
            start = mid+1
        elif card[mid] > i:
            end = mid-1

    if check == 1:
        print("1", end=" ")
    else:
        print("0",end=" ")
