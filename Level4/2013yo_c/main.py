from itertools import product

N = int(input())
S = input()
D = [input() for _ in range(N)]

def valid(d):
    if S == d:
        return True
    elif len(S) > len(D):
        return False
    else:
        prev = -1
        indices = [
            [i for i in range(len(d)) if d[i] == S[k]]
            for k in range(len(S))
        ]
        # print(S, d)

        for p in product(*indices):
            flag = True
            for j in range(1, len(p)):
                if p[j - 1] > p[j]:
                    flag = False
            if flag:
                diffs = [p[j] - p[j - 1] for j in range(1, len(p))]
                if len(set(diffs)) == 1:
                    return True
        return False

count = 0
for d in D:
    if valid(d):
        count += 1

print(count)