def prod(a,b):
    if a==0:
        return b
    elif b ==0:
        return a
    else:
        return a + prod(a,b-1)
        