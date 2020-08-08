nums = set({})
for _ in range(28):
    n = int(input())
    nums.add(n)

for k in range(1, 31):
    if k not in nums:
        print(k)