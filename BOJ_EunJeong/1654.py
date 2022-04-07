K,N = map(int,input().split())
l = list()

for i in range(K):
    l.append(int(input()))

start,end = 1,max(l)

while start <= end:
    mid = (start+end)//2
    result = 0
    for i in l:
        result += i//mid
    if result >= N:
        start = mid + 1
    else:
        end = mid -1
        
print(end)
