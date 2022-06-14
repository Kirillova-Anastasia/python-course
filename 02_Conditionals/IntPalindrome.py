def get_number(n, k):
    for i in range(k-1):
        n = n // 10
    return n % 10

n = int(input())
t = 0
while 10**t <= n:
    t += 1
k = 1
palindrom = True
while palindrom and t > k:
    palindrom =  get_number(n, t) == get_number(n, k)
    t -= 1
    k += 1
print('YES' if palindrom else 'NO')

