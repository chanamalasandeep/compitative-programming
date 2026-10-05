s = input().strip()
seen = 0
duplicates = []
printed = 0
for ch in s:
    bit = 1 << (ord(ch) - ord('a'))
    if seen & bit:
        if not (printed & bit):
            duplicates.append(ch)
            printed |= bit
    else:
        seen |= bit
if duplicates:
    print(*duplicates)
else:
    print("No duplicates")
    
