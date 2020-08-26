N = int(input())
S = [[0,i] for i in range(N)]
for _ in range(N * (N - 1) // 2):
    A, B, C, D = map(int, input().split())
    A, B = A - 1, B - 1
    if C < D:
        S[B][0] += 3
    elif C > D:
        S[A][0] += 3
    else:
        S[A][0] += 1
        S[B][0] += 1

S.sort(reverse=True)
prev = 10 ** 10
order = 0
ans = [-1] * N
for i, (scores, v) in enumerate(S):
    if prev > scores:
        order = i + 1
    ans[v] = order
    prev = scores

for v in ans:
    print(v)