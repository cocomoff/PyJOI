def calc(h1, m1, s1, h2, m2, s2):
    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2
    dt = t2 - t1
    h = dt // 3600
    dt -= h * 3600
    m = dt // 60
    dt -= m * 60
    return (h, m, dt)

for _ in range(3):
    arg = list(map(int, input().split()))
    print(*calc(*arg))