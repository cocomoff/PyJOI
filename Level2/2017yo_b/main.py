# 2Nマス M枚
N, M = map(int, input().split())

# あたりai はずれbi
A, B, cost = [], [], []
for _ in range(M):
    ai, bi = map(int, input().split())
    A.append(ai)
    B.append(bi)

    if ai >= N:
        cost.append(0)
    else:
        cost.append(N - ai)

cost.sort()
print(sum(cost[:-1]))