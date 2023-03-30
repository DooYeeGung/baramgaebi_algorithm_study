# 상하좌우

import numpy as np

n = int(input())

task = list(map(str, input().split()))

dir = {
    'L': np.array([0,-1]),
    'R': np.array([0,1]),
    'U': np.array([-1,0]),
    'D': np.array([1,0]),
}

s = np.array([1,1])

for t in task:
    tmp = s + dir[t]

    if (tmp[0] > n or tmp[0] < 1) or (tmp[1] > n or tmp[1] < 1):
        continue
    else:
        s = tmp

print(s[0], s[1])