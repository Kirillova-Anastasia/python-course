def divdigit(n):
    tmp = n
    res = 0
    while tmp > 0:
        d = tmp % 10
        tmp //= 10
        if d and n % d == 0:
            res += 1
    return res
