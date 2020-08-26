N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
cur = 1

for i in range(M):
    m = int(input())
    cur += m

    if cur >= N:
        print(i + 1)
        exit()

    cur += A[cur - 1]

    if cur >= N:
        print(i + 1)
        exit()
