# https://atcoder.jp/contests/joi2007yo/tasks/joi2007yo_d

n = int(input())
m = int(input())
card = [i for i in range(1, 2 * n + 1)]

for _ in range(m):
    k = int(input())
    new_card = []
    if k == 0:
        # リフルシャッフル
        for i in range(n):
            new_card.append(card[i])
            new_card.append(card[i + n])
    else:
        # k-カット
        new_card = card[k:] + card[:k]
    card = new_card

for c in card:
    print(c)

