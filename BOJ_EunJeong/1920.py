def binary_search(arr,target):
    start,end = 0,len(arr)-1
    while start<=end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid]>target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

A.sort()

for i in B:
    if binary_search(A,i):
        print("1")
    else:
        print("0")
