def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    r = ""
    for l in s:
        r += l if l.lower() not in "aeiou" or not l.isalpha() else ""
    print(r)

print_without_vowels("This is great!")
