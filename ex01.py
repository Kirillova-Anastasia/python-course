def f(a, L=None):
    print(a, L)
    if L is None:
        L = []
    print(a,L)
    L.append(a)
    return L

print(f(1))
print()
print(f(2))
print()
print(f(3))
