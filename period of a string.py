s = input().strip()

n = len(s)


lps = [0] * n
j = 0

for i in range(1, n):
    while j > 0 and s[i] != s[j]:
        j = lps[j - 1]

    if s[i] == s[j]:
        j += 1

    lps[i] = j


p = n - lps[-1]


if n % p == 0:
    print(p)
else:
    print(n)
