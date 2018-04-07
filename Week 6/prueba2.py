import random
le = 1000
L = [random.randint(0, le) for i in range(le)]

c = 0

def mySort(L):
    """ L, list with unique elements """
    global c
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                c += 1
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def newSort(L):
    """ L, list with unique elements """
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
mySort(L1)
print(c)
c = 0
newSort(L2)
print(c)

print(L1 == L2)

