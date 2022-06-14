def det(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    res = 0
    for i in range(n):
        b = [[a[k][j] for j in range(n) if j != i] for k in range(1,n)]
        res += a[0][i] * det(b) * (-1)**i
    return res

a = list(eval(input()))
a = [list(x) for x in a]
print(det(a))