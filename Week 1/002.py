s = 'azcbobobegghakl'
p = "bob"

count = 0
for i in range(len(s)):
    j, k = i, 0
    while k < len(p) and j < len(s) and s[j] == p[k]:
        if k == len(p)-1:
            count += 1
        j, k = j+1, k+1

print("Number of times bob occurs is:", count)
