import sys
input = sys.stdin.readline

id = list(input())
del id[len(id)-1]

for i in id:
    print(i,end='')
print("??!")
