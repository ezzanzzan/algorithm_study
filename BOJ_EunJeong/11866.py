import sys
input = sys.stdin.readline

N,K = map(int,input().split())
Queue = [i for i in range(1,N+1)]
result = []

while Queue:
    num = K
    while num > len(Queue):
        num = num - len(Queue)
    result.append(Queue[num-1])
    del Queue[num-1]
    a = Queue[:num-1]
    b = Queue[num-1:]
    Queue = b + a

print("<",end="")
for i in range(len(result)-1):
    print(result[i],end = ", ")
print(result[N-1],end=">")
