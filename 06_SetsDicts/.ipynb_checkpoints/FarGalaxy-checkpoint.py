galaxies = {}
max_d = 0
g1, g2 = '', ''

s = input()
while ' ' in s:
    x, y, z, name = s.split()
    x, y, z = float(x), float(y), float(z)
    for galaxy, name1 in galaxies.items():
        x1, y1, z1 = galaxy
        d = (x1-x)**2 + (y1-y)**2 + (z1-z)**2
        if d > max_d:
            max_d = d
            g1, g2 = min(name, name1), max(name, name1) 
    galaxies[(x,y,z)] = name
    s = input()
print(g1, g2)
        
    