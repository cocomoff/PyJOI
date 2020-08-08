# https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_a

from itertools import accumulate

N, K = map(int, input().split())
A = [0] + [int(input()) for _ in range(N)]
cA = list(accumulate(A))
# print(A)
# print(cA)

mv = -(10 ** 10)
for k in range(N - K + 1):
    mv = max(cA[k + K] - cA[k], mv)
    # print(k, cA[k], cA[k - 3])
print(mv)