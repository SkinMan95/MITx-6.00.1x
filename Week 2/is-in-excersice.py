def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = len(aStr) // 2
    if len(aStr) > 1:
        if aStr[mid] == char:
            return True
        else:
            return isIn(char, aStr[mid:]) if aStr[mid] < char else isIn(char, aStr[:mid])
    return len(aStr) == 1 and aStr == char


print(isIn("e", "abcde"))
print(isIn("a", "abcde"))
print(isIn("b", "abcde"))
print(isIn("e", "abcd"))
print(isIn("a", "bcde"))
print(isIn("c", "abde"))
