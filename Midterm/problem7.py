def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invd = {}
    for val in d.keys():
        if d[val] in invd.keys():
            invd[d[val]].append(val)
        else:
            invd[d[val]] = [val]

    for k in invd.keys():
        invd[k].sort()

    return invd

print(dict_invert({1:10, 2:20, 3:30}))
print(dict_invert({1:10, 2:20, 3:30, 4:30}))
print(dict_invert({4:True, 2:True, 0:True}))
