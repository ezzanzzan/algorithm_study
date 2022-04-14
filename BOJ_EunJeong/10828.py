import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    Command = input()
    if Command == 'top\n':
        if not stack:
            print("-1")
        else:
            print(stack[-1])
    elif Command == 'pop\n':
        if not stack:
            print("-1")
        else:
            print(stack[-1])
            stack.pop()
    elif Command == 'size\n':
        print(len(stack))
    elif Command == 'empty\n':
        if not stack:
            print("1")
        else:
            print("0")
    else:
        num= Command[5:]
        stack.append(int(num))
