graph = {}
s = input()
while ' ' in s:
    v1, v2 = s.split()
    if v1 in graph:
        graph[v1].append(v2)
    else:
        graph[v1] = [v2]
    if v2 in graph:
        graph[v2].append(v1)
    else:
        graph[v2] = [v1]
    s = input()
start = s
end = input()

accessible = (start == end)
last = set([start])
while not accessible and last:
    curr = []
    for v in last:
        if v in graph:
            curr.extend(graph[v])
            graph.pop(v)
    last = set(curr)
    accessible = end in last
print('YES' if accessible else 'NO')
            
    
