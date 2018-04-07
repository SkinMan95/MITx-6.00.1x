s = 'azcbobobegghakl'
#s = "abcbcd"

mx = 1 if len(s) > 0 else 0
sub = s[0] if len(s) > 0 else ""

for i in range(len(s)):
    l, j = 0, i
    while j < len(s)-1 and s[j] <= s[j+1]:
        l = j -i +2
        j += 1
    if mx < l:
        # print("si")
        sub = s[i:i+l]
        mx = l

print("Longest substring in alphabetical order is:", sub)
