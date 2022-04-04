N = int(input())
list = []

while N>1:
    for i in range(2,N+1):
        while N%i == 0:
            N = int(N/i)
            list.append(i)

list.sort()
for i in list:
    print(i)
