from time import time

# t1 = time()
seq = set(eval(input()))
M = max(seq)

sqrs = [i*i + j*j + k*k for i in range(1, int((M/3)**0.5) + 1)
        for j in range(i, int(((M-i*i)/2)**0.5) + 1)
        for k in range(j, int((M-i*i-j*j)**0.5) + 1) if i*i + j*j + k*k in seq]
            
print(len(set(sqrs)))
# print('Time is ', time()-t1)