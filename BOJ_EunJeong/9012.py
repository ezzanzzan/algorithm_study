import sys
input = sys.stdin.readline

T = int(input())

for n in range(T):
    S = input()
    temp = True
    check = []
    for i in S:
        if i == '(' or i == '[':
            check.append(i)
        elif i == ')':
            if not check or check[-1] == '[':
                temp = False
                break
            elif check[-1] == '(':
                check.pop()
        elif i == ']':
            if not check or check[-1] == '(':
                temp = False
                break
            elif check[-1] == '[':
                check.pop()
    if not check and temp:
        print("YES")
    else:
        print("NO")
