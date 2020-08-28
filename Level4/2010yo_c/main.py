INF = 10 ** 9
n = int(input())
m = int(input())
g = [[INF] * n for _ in range(n)]

for _ in range(m):
    ai, bi = map(lambda x: int(x) - 1, input().split())
    g[ai][bi] = 1
    g[bi][ai] = 1

# Floyd-warshall algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

ans = 0
for u in range(1, n):
    if g[0][u] <= 2:
        ans += 1
print(ans)