S = input()
ans = ''
for ch in S:
    n = ord(ch) - 3
    if n < 65:
        n += 26
    ans += chr(n)
print(ans)