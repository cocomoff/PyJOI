from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
cA = Counter(A)
print(cA.most_common()[0][1])