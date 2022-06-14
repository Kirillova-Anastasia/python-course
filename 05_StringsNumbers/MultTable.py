n, m = eval(input())

first_w = 1
while 10 ** first_w <= n:
    first_w += 1
    
n_2 = n*n
second_w = 1
while 10 ** second_w <= n_2:
    second_w += 1
    
w = 2 * first_w + second_w + 6
num_columns = 1 + (m - w) // (w + 3)

strs = [['='*m]]
for i in range(n):
    for j in range(n):
        pos = i // num_columns * (n+1) + 1 + j
        if i % num_columns == 0:
            strs.append(['{0:{width}d}'.format(i+1, width=first_w)])
            strs[-1].append(' * ')
            strs[-1].append('{0:<{width}d}'.format(j+1, width=first_w))
            strs[-1].append(' = ')
            strs[-1].append('{0:<{width}d}'.format((i+1)*(j+1), width=second_w))
        else:
            strs[pos].append(' | ')
            strs[pos].append('{0:{width}d}'.format(i+1, width=first_w))
            strs[pos].append(' * ')
            strs[pos].append('{0:<{width}d}'.format(j+1, width=first_w))
            strs[pos].append(' = ')
            strs[pos].append('{0:<{width}d}'.format((i+1)*(j+1), width=second_w))
    if i % num_columns == num_columns - 1:
        strs.append(['='*m])
if i % num_columns != num_columns - 1:
    strs.append(['='*m])

for l in strs:
    print(''.join(l))
                        