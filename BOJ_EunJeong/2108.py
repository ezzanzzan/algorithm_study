from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

num.sort()
num1 = Counter(num).most_common(2)

a = f'{sum(num)/len(num):.0f}'
if str(a) =='-0':
    print("0")
else:
    print(a)

print(num[len(num)//2])

if len(num1)>1:
    if num1[0][1]==num1[1][1]:
        print(num1[1][0])
    else:
        print(num1[0][0])
else:
    print(num1[0][0])
print(num[-1]-num[0])
