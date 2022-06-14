k = int(input())
if k == 1:
    print(1)
    exit()

p = 10*k - 1
n = 1
while (10**n - k) % p:
    n += 1
    
a_ = k*(10**n - k) // p
print(a_*10 + k) 