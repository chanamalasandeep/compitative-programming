n = int(input())
arr = list(map(float, input().split()))


if max(arr) >= 1:
    min_val = min(arr)
    max_val = max(arr)

    buckets = [[] for _ in range(n)]

    for x in arr:
        if max_val == min_val:
            index = 0
        else:
            index = int((x - min_val) / (max_val - min_val) * n)
            if index == n:
                index = n - 1

        buckets[index].append(x)

else:
    
    buckets = [[] for _ in range(n)]

    for x in arr:
        index = int(x * n)
        buckets[index].append(x)

for bucket in buckets:
    bucket.sort()

result = []
for bucket in buckets:
    result.extend(bucket)


print(" ".join(f"{x:.2f}" if x % 1 != 0 else f"{int(x)}" for x in result))
