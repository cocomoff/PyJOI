N = int(input())
X = list(map(int, input().split()))
M = int(input())
A = list(map(int, input().split()))

for a in A:
    if a == N or X[a - 1] + 1 not in X:
        if X[a - 1] < 2019:
            X[a - 1] += 1

for x in X:
    print(x)