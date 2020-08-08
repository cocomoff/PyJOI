N = int(input())
M = int(input())
target = list(map(int, input().split()))
users = [list(map(int, input().split())) for _ in range(M)]
scores = [0] * N

for k in range(M):
    count = 0
    for u in range(N):
        if users[k][u - 1] != target[k]:
            count += 1
        else:
            scores[u - 1] += 1
        pass
    scores[target[k] - 1] += count

for s in scores:
    print(s)