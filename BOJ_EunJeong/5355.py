T = int(input())

for i in range(T):
    test = input().split()
    sum = float(test[0])
    for j in test:
       if j == '@':
           sum = sum*3
       elif j == '%':
           sum = sum+5
       elif j =='#':
           sum = sum-7
    print(f'{sum:.2f}')
