def majorityElement(arr):
    candidate = None
    count = 0

    # Find a candidate
    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    # Verify the candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1

n = int(input())
arr = list(map(int, input().split()))

print(majorityElement(arr))
