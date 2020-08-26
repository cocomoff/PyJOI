N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

count = [0] * (1001)

for k in range(M):
    Bk = B[k]
    jj = [n for n in range(N) if A[n] <= Bk]
    count[jj[0] + 1] += 1

print(count.index(max(count)))