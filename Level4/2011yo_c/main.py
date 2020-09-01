# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_c

N = int(input())
K = int(input())
AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]
# AB = [tuple(map(int, input().split())) for _ in range(K)]

# red: 0, 3, 6, ...
# blue: 1, 4, 7, ...
# yellow: 2, 5, 8, ...

for (a, b) in AB:
    # 左上にもってくる
    a = min(a, N - a - 1)
    b = min(b, N - b - 1)
    if a < b:
        a, b = b, a

    print(b % 3 + 1)
