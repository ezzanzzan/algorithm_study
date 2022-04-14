import sys
input = sys.stdin.readline

N = int(input())
n_card = list(map(int,input().split()))
M = int(input())
m_card = list(map(int,input().split()))

result = []
card = m_card[::]
m_card = list(set(m_card))
n_card.sort()
m_card.sort(reverse=True)

for i in m_card:
    num = 0
    while n_card and i <= n_card[-1]:
        if i == n_card[-1]:
            num += 1
        n_card.pop()
    add = (i,num)
    result.append(add)

for i in card:
    start, end = 0, len(result)-1
    while start<=end:
        mid = (start+end)//2
        if i == result[mid][0]:
            print(result[mid][1],end=' ')
            break
        elif i < result[mid][0]:
            start = mid + 1
        elif i > result[mid][0]:
            end = mid - 1
