def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    r = tuple()
    for i in range(len(aTup)):
        if (i % 2 == 0):
            r = r + (aTup[i],)
    return r
