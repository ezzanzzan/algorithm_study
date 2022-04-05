S = int(input())
N = 0
num = 0

for i in range(1,S+1):
    N = N + i
    num += 1
    if S==N:
        break
    elif N>S:
        num -= 1
        break
print(num)
