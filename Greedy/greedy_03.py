# 숫자 카드 게임

n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

mini = 0

for i in range(n):
    tmp = min(lst[i])
    if tmp > mini:
        mini = tmp

print(mini)