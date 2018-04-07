import string

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    assert isinstance(s, str), 'not a string'
    found = False
    sum = 0
    for i in s:
        if i in string.digits:
            found = True
            sum += int(i)

    if found == False:
        raise ValueError("input string does not contain any digit")

    return sum
            
print(sum_digits("a;35d4"))
print(sum_digits("a;d"))
