begin = input()
cnt = 0
n = len(begin)
prev = [0 for i in range(n)]

s = input()
while s != begin:
    for i in range(1, n):
        if s[i] == '#':
            if s[i-1] == '.' and not prev[i]:
                cnt += 1
            prev[i] = 1
        else:
            prev[i] = 0
    s = input()
print(cnt)