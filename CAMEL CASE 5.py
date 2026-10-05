n=int(input())
words=input().strip().split(",")
pattern=input().strip()
matches=[]
for word in words:
    abbreviation = ""
    for ch in word:
        if ch.isupper():
            abbreviation += ch
    i = 0
    for ch in abbreviation:
        if i < len(pattern) and ch==pattern[i]:
            i+=1
    if i==len(pattern):
        matches.append((abbreviation, word))
matches.sort(key=lambda x: (x[0], x[1]))
if not matches:
    print("No match found")
else:
    for abbreviation, word in matches:
        print(word)
