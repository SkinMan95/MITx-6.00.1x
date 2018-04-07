def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    assert isinstance(t, (int, tuple, list)), 'not an int, a tuple or a list'
    assert isinstance(t, int) or len(t) > 0, 'list or tuple is empty'

    max_e = float("-inf")
    if not isinstance(t, int):
        for e in t:
            assert isinstance(t, (int, tuple, list)), 'not every (sub)element of input is ' + \
                'an int, a tuple or a list'
            max_e = max(max_e, (e if isinstance(e, int) else max_val(e)))
    else:
         max_e = t

    assert isinstance(max_e, int)
    return max_e


assert max_val((5, (1,2), [[1],[2]])) == 5
assert max_val((5, (1,2), [[1],[9]])) == 9

print(max_val((5, (1,2), [[1],[2]])))
print(max_val((5, (1,2), [[1],[9]])))
