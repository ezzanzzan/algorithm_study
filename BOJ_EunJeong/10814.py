import sys
input = sys.stdin.readline

N = int(input())
member=[]
for i in range(N):
    a,b=input().split()
    add = (int(a),b,int(i))
    member.append(add)

member.sort(key=lambda x:(x[0],x[2]))

for i in range(len(member)):
    print(member[i][0],member[i][1])
