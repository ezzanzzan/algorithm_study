n = int(input())
arr = []
stack = []
result = []
j = 1

for i in range(n):
    arr.append(int(input()))

for i in arr:
    while j <= n+1:
        if not stack:
            stack.append(j)
            result.append("+")
            j += 1
        else:
            if i == stack[-1]:
                stack.pop()
                result.append("-")
                break
            else:
                stack.append(j)
                result.append("+")
                j += 1

if not stack:
    for i in result:
        print(i)
else:
    print("NO")
