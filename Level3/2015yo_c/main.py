H, W = map(int, input().split())
ans = [[-1] * W for _ in range(H)]

for h in range(H):
    s = input()
    for w in range(W):
        if s[w] == 'c':
            ans[h][w] = 0
        else:
            if w >= 1:
                if ans[h][w - 1] >= 0:
                    ans[h][w] = ans[h][w - 1] + 1

for a in ans:
    print(*a)