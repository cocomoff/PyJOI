# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_b

S = input()
n = int(input())
count = 0
for _ in range(n):
    si = input()
    si *= 2
    if S in si:
        count += 1
print(count)