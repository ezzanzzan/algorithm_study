import sys
input = sys.stdin.readline

while True:
    S = input()
    if S == '.\n':
        break
    temp = True
    check = []
    for i in S:
        if i == '[' or i == '(':
            check.append(i)
        elif i == ']':
            if not check or check[-1] == '(':
                temp = False
                break
            elif check[-1] == '[':
                check.pop()
        elif i == ')':
            if not check or check[-1]=='[':
                temp = False
                break
            elif check[-1] == '(':
                check.pop()

    if temp and not check:
        print('yes')
    else:
        print('no')
