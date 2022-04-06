N = int(input())
arr = list()

for i in range(N):
    arr.append((input()))

result = list(set(arr))

result.sort()
result.sort(key=lambda x:len(x))

for i in result:
    print(i)
