a, b, c = map(int, input().split())
check = [2] * (a + b + c)
n = int(input())
x = []

for _ in range(n):
    ai, bi, ci, di = map(int, input().split())
    ai, bi, ci = ai - 1, bi - 1, ci - 1
    if di == 1:
        check[ai] = check[bi] = check[ci] = 1
    else:
        x.append((ai, bi, ci))

for t in x:
    # 複数回試されて，ngの場合は壊れている
    ti = [i for i in t if check[i] != 1]
    if len(ti) < 2:
        check[ti[0]] = 0

for row in check:
    print(row)