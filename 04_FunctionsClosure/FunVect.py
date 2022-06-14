def superposition(funmod, funseq):
    res = []
    for fun in funseq:
        def caller(x, fun=fun):
            return funmod(fun(x))
        res.append(caller)
    return res

# from time import time
# begin = time()
# # from math import *
# # F = superposition(abs, (sin, cos))
# # print(F[0](-1), F[1](-1), F[0](2), F[1](2))
# N = 3000
# funs = [lambda l, n=i: [x % n for x in l] for i in range(2, N)]
# print(*(f(range(0, (N//2)*(N**2-1), N**2-1)) for f in superposition(max, funs)))
# print(time() - begin)
