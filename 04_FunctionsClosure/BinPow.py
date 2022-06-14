def BinPow(a, n, f):
    if n == 1:
        return a
    if n % 2: #нечетное
        return f(a, BinPow(a, n-1, f))
    #четное
    tmp = BinPow(a, n/2, f)
    return f(tmp, tmp)



