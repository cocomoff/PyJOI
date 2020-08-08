A, B, C = map(int, input().split())

current = 0
day = 0
while current < C:
    day += 1
    current += A
    if day % 7 == 0:
        current += B
print(day)