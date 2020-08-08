# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_b

from collections import defaultdict

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
scores = [0] * n

for k in range(3):
    sc = defaultdict(int)
    for u in range(n):
        sc[nums[u][k]] += 1
    for u in range(n):
        if sc[nums[u][k]] == 1:
            scores[u] += nums[u][k]

for s in scores:
    print(s)