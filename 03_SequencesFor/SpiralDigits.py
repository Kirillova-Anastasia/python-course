m,n = [int(x) for x in input().split(',')]

a = [[0 for i in range(m)] for j in range(n)]
x1, x2, y1, y2 = 0, m-1, 0, n-1
num = 0

def step(y1, y2, x1, x2):
    return y1+1, y2-1, x1+1, x2-1

while (y1 <= y2 and x1 <= x2):
    for i in range(x1, x2+1):
        a[y1][i] = num
        num = (num + 1) % 10
    for i in range(y1+1, y2):
        a[i][x2] = num
        num = (num + 1) % 10
    if y2 == y1:
        y1, y2, x1, x2 = step(y1, y2, x1, x2)
        break
    for i in range(x2, x1-1, -1):
        a[y2][i] = num
        num = (num + 1) % 10
    if x2 == x1:
        y1, y2, x1, x2 = step(y1, y2, x1, x2)
        break
    for i in range(y2-1, y1, -1):
        a[i][x1] = num 
        num = (num + 1) % 10
    y1, y2, x1, x2 = step(y1, y2, x1, x2)    

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
            
