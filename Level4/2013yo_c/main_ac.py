from itertools import product

N = int(input())
S = input()
D = [input() for _ in range(N)]

def valid(d):
    # 開始地点
    # print(S, d)
    for i in range(len(d) - len(S) + 1):
        # ステップ数
        for j in range(1, len(d) + 1):
            # print(i, j, d[i:i+j*len(S):j])
            if d[i:i+j*len(S):j] == S:
                return True
    return False

count = 0
for d in D:
    if valid(d):
        count += 1

print(count)