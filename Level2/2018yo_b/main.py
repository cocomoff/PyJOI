N = int(input())
A = list(map(int, input().split()))

# 連続する1の最大長 + 1
now = 0
max_length = 0
length = 0
while now < N:
    if A[now] == 1:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0
    now += 1
max_length = max(max_length, length)

print(max_length + 1)