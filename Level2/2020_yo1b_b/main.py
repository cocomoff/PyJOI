N, A, B = map(int, input().split())
A -= 1
S = input()
SS = S[:A] + S[A:B][::-1] + S[B:]
print(SS)