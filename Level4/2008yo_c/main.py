from collections import deque

n = int(input())
taro = [int(input()) for _ in range(n)]
taro.sort()
taro = deque(taro)
hanako = [n for n in range(1, 2 * n + 1) if n not in taro]
hanako = deque(hanako)

# print(taro, hanako)
current = None

while len(taro) > 0 and len(hanako) > 0:
    # taro
    cur_taro = None
    if current is None:
        cur_taro = taro[0]
    else:
        for elem in taro:
            if elem > current:
                cur_taro = elem
                break
    if cur_taro is not None:
        current = cur_taro
        taro.remove(cur_taro)
    else:
        current = None

    if len(taro) == 0:
        break
    
    # hanako
    cur_hanako = None
    if current is None:
        cur_hanako = hanako[0]
    else:
        for elem in hanako:
            if elem > current:
                cur_hanako = elem
                break
    if cur_hanako is not None:
        current = cur_hanako
        hanako.remove(cur_hanako)
    else:
        current = None

print(len(hanako))
print(len(taro))