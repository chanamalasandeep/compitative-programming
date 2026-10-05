
i, j = map(int, input().split())
orig_i, orig_j = i, j
if i > j:
    i, j = j, i
memo = {1: 1}
def cycle_length(n):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        memo[n] = 1 + cycle_length(n // 2)
    else:
        memo[n] = 1 + cycle_length(3 * n + 1)
    return memo[n]
max_cycle = 0
for num in range(i, j + 1):
    max_cycle = max(max_cycle, cycle_length(num))
print(orig_i,orig_j,max_cycle)
