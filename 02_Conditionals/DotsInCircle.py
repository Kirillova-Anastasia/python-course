x, y, r = eval(input())
flag = True
while flag:
    a, b = eval(input())
    if not (a or b):
        break
    if (x-a)**2 + (y-b)**2 > r*r:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
