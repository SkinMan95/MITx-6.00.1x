def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    assert all(isinstance(i, str) for i in (map_from, map_to, code)), 'not all inputs are strings'
    assert all(i in map_from for i in code), 'not every letter in map_from'
    assert len(map_from) == len(map_to), 'maps must be of same length'

    key_code, decoded = dict(), ""

    for i in range(len(map_from)):
        f, t = map_from[i], map_to[i]
        assert f not in key_code.keys() or key_code[f] == t
        
        key_code[f] = key_code.get(f, t)

    for letter in code:
        assert letter in key_code.keys()
        decoded += key_code[letter]

    return (key_code, decoded)


assert cipher("abcd", "dcba", "dab") == ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
print(cipher("abcd", "dcba", "dab"))
