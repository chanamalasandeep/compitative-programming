n = int(input())
a = list(map(int, input().split()))
total = sum(a)
k = n // 2
ans = total
def solve(i, count, s):
    global ans
    if count == k:
        ans = min(ans, abs(total - 2 * s))
        return
    if i == n:
        return
    solve(i + 1, count + 1, s + a[i])
    solve(i + 1, count, s)
solve(0, 0, 0)
print(ans)
