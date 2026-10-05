
x, y = map(int, input().split())
if y == 0:
    print("Division by zero")
else:
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)
    low, high = 0, x
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * y == x:
            ans = mid
            break
        elif mid * y < x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(sign * ans)
