import math
data = list(map(int, input().split()))
if len(data) == 3:
    A, B, T = data
    if T <= max(A, B) and T % math.gcd(A, B) == 0:
        print("YES")
    else:
        print("NO")

else:
    Q = data[0]
    for i in range(Q):
        A, B, T = data[1 + i * 3: 4 + i * 3]
        if T <= max(A, B) and T % math.gcd(A, B) == 0:
            print("YES")
        else:
            print("NO")
