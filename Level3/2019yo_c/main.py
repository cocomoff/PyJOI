n = int(input())
S = input()

i = 0
count = 0
while i < n - 1:
    if S[i] == S[i + 1]:
        i += 1
    else:
        count += 1
        i += 2

print(count)
