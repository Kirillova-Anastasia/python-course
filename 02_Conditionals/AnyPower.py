def is_pow(n, k):
    while n > 1:
        if n % k:
            return False
        n = n / k
    return True

n = int(input())
answ = False
for i in range(2, int(n**0.5)+1):
    if is_pow(n, i):
        answ = True
        break
print('YES' if answ else 'NO')
