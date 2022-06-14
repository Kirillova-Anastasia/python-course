def squares(w,h, *rects):
    ss = ['.' * w for i in range(h)]
    for x, y, s, c in rects:
        for row in range(y,y+s):
            ss[row] = ss[row][:x] + c * s + ss[row][x+s:]
    for st in ss:
        print(st)