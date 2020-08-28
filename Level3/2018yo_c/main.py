H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

cost = 10 ** 10

for h in range(H):
    for w in range(W):
        cost_hw = 0
        # print(h, w)
        for hh in range(H):
            for ww in range(W):
                if hh != h and ww != w:
                    # print(" ", hh, ww)
                    cost_hw += min(abs(hh - h), abs(ww - w)) * A[hh][ww]
        cost = min(cost, cost_hw)
print(cost)