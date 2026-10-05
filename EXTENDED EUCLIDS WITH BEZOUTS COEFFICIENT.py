import math
A, B = map(int, input().split())
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y
D, x0, y0 = extended_gcd(A, B)
p = B // D
q = A // D
candidates = set()
k = (-x0) // p
candidates.add(k)
candidates.add(k + 1)
k = y0 // q
candidates.add(k)
candidates.add(k + 1)
best = None
for k in candidates:
    x = x0 + k * p
    y = y0 - k * q
    value = abs(x) + abs(y)
    if best is None:
        best = (value, x, y)
    elif value < best[0]:
        best = (value, x, y)
    elif value == best[0] and x <= y and best[1] > best[2]:
        best = (value, x, y)

print(best[1], best[2], D)
