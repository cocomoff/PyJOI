N = int(input())
A = list(map(int, input().split()))
c = 0

for i in range(N):
    pre = A[i]
    cur = 1
    for j in range(1, N - i):
        if pre <= A[i + j]:
            cur += 1
            pre = A[i + j]
        else:
            break
    c = max(c, cur)
print(c)