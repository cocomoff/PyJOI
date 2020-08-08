# https://atcoder.jp/contests/joi2007yo/tasks/joi2007yo_f

C, R = map(int,input().split())

dp = [[0] * (C + 1) for _ in range(R + 1)]
dp[0][0]=1

K = int(input())
loc = set({})
for _ in range(K):
    xi, yi = map(int, input().split())
    loc.add((xi - 1, yi - 1))


for i in range(R):
    for j in range(C):
        if (j, i) in loc:
            continue
        dp[i+1][j] += dp[i][j]
        dp[i][j+1] += dp[i][j]

print(dp[-2][-2])