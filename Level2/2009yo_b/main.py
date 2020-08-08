# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_b

W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]
W.sort()
K.sort()

w = W[-1] + W[-2] + W[-3]
k = K[-1] + K[-2] + K[-3]

print(w, k)
