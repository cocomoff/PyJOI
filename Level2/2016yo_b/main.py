# https://atcoder.jp/contests/joi2016yo/tasks/joi2016yo_b

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

for i in range(1, M + 1):
    for j in range(N - 1):
        if A[j] % i > A[j + 1] % i:
            A[j], A[j + 1] = A[j + 1], A[j]
for i in A:
    print(i)