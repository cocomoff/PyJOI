# https://atcoder.jp/contests/joisc2007/tasks/joisc2007_score

N = int(input())
scores = [int(input()) for _ in range(N)]
S = sorted(scores, reverse=True)
ranks = {}
count = 1
for s in S:
    if s not in ranks:
        ranks[s] = count
        count += 1
    else:
        count += 1

for s in scores:
    print(ranks[s])