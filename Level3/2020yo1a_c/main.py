N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A + B)
for c in C:
    print(c)