# 거스름돈

n = int(input())
coin = [500, 100, 50, 10]
cnt = 0

cash = n
for i in coin:
    num = cash//i
    cash -= i * num # cash %= i
    cnt += num

print(cnt)