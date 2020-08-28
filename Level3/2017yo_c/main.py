N, M, D = map(int, input().split())
S = [input() for _ in range(N)]
count = 0

# 横方向
for n in range(N):
    for m in range(M - D + 1):
        if '#' not in S[n][m:m+D]:
            count += 1

# 縦方向
for m in range(M):
    for n in range(N - D + 1):
        ss = "".join([S[n+i][m] for i in range(D)])
        if "#" not in ss:
            count += 1

print(count)