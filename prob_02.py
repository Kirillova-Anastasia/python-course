ps = [float(x) for x in input().split()]
xs = [float(x) for x in input().split()]
n = len(ps)

weighted_sum = 0
for i in range(n):
    weighted_sum += ps[i]*xs[i]

#std = 0
#for i in range(n):
#    std += (xs[i] - weighted_sum)**2
#std = (std/n)**0.5

variance = 0
for i in range(len(xs)):
   variance += ps[i] * (xs[i] - weighted_sum)**2

std = variance**0.5

print(weighted_sum, round(std, 2), round(variance, 2))
