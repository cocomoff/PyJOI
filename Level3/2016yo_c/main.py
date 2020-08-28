N, M = map(int, input().split())
S = [input() for _ in range(N)]

# white/blue/redの位置
# [0, w), [w, b), [b, N)
ans = N * M + 1
for w in range(1, N - 1):
    for b in range(w + 1, N):
        # non-white in [0, w)
        c = 0
        for k in range(w):
            for m in range(M):
                if S[k][m] != 'W':
                    c += 1
        # non-blue in [w, b)
        for k in range(w, b):
            for m in range(M):
                if S[k][m] != 'B':
                    c += 1
        # non-red in [b, N)
        for k in range(b, N):
            for m in range(M):
                if S[k][m] != 'R':
                    c += 1
        ans = min(ans, c)

print(ans)