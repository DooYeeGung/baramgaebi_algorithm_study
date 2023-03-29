# 큰 수의 법칙

n, m, k = map(int, input().split(" "))
lst = list(map(int, input().split()))

lst.sort()

max0 = lst[-1]
max1 = lst[-2]
print(max0, max1)

loop = m//(k+1)
ex = m%(k+1)

tmp = max0 * (loop*k + ex) + max1 * loop

result = tmp

print(result)