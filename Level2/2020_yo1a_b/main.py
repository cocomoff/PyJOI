from collections import Counter

N = int(input())
S = input()
cS = Counter(S)
vowel = ['a', 'i', 'u', 'e', 'o']
ans = 0
for c in vowel:
    ans += cS[c]
print(ans)