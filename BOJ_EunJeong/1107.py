import sys
input = sys.stdin.readline

target = int(input())   # 이동하려고 하는 채널
M = int(input())        # 고장난 버튼의 개수
channel = 100           # 현재 채널
num = abs(target - channel) # +,-를 이용해서 이동하려고 하는 채널까지 누르는 횟수

if M:   # 고장난 버튼이 있을 때
    broken = list(input().split())

    # 이동하려고 하는 채널의 범위가 0~500,000이고 채널은 무한대까지 있기 때문에 두 배인 1,000,000까지를 범위로 잡아준다
    for n in range(1000001):
        n = str(n)
        for i in n:
            # 이동하려는 채널 중 고장난 버튼이 있다면 다음 채널으로 넘어간다.
            if i in broken:
                break
            # 이동하려는 채널 중 고난장 버튼이 없다면
        else:
            # target 채널으로 이동하기 위해 최소 눌러야 하는 버튼의 수를
            # 위에 계산한 횟수와 채널 n에서 target 채널으로 이동하기 위해 누르는 버튼 수 중 최솟값으로 업데이트 해준다.
            num = min(num,len(n)+abs(int(n)-target))
else:   # 고장난 버튼이 없을 경우
    num = min(num,len(str(target)))

print(num)
