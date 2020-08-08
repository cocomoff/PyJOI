# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_b

joi, ioi = 0, 0
S = input()
for i in range(len(S) - 2):
    si = S[i:i+3]
    if si == 'JOI':
        joi += 1
    elif si == 'IOI':
        ioi += 1
print(joi)
print(ioi)