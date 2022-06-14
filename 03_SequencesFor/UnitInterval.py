pairs = list(eval(input()))
pairs.sort()
#print(pairs)

sum = 0
i = 0
begin, end = 0, 0

while i < len(pairs):
    sum += end - begin
    begin = pairs[i][0]
    end = pairs[i][1]

    i += 1
    while i < len(pairs) and pairs[i][0] <= end:
        end = max(end, pairs[i][1])
        i += 1
sum += end - begin

print(sum)
