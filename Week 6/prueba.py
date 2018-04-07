import random
le = 1000
L = [random.randint(0, le) for i in range(le)]

c = 0

def selSort(L):
    global c
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            c += 1
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

def newSort(L):
    global c
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                c += 1
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1


L1 = L[:]
L2 = L[:]

c = 0
selSort(L1)
print(c)
c = 0
newSort(L2)
print(c)

print(L1 == L2)
