xi=float(input('digite x inicial:'))
yi=float(input('digite y inicial:'))
x1=float(input('digite x1:'))
y1=float(input('digite y1:'))
x2=float(input('digite x2:'))
y2=float(input('digite y2:'))
x3=float(input('digite x3:'))
y3=float(input('digite y3:'))
x4=float(input('digite x4:'))
y4=float(input('digite y4:'))
d1=abs(x1-xi)+abs(y1-yi)
d2=abs(x2-xi)+abs(y2-yi)
d3=abs(x3-xi)+abs(y3-yi)
d4=abs(x4-xi)+abs(y4-yi)
if d1<d2 and d1<d3 and d1<d4:
    print('hospital 1')
elif d2<d1 and d2<d3 and d2<d4:
    print('hospital 2')
elif d3<d1 and d3<d2 and d3<d4:
    print('hospital 3')
else:
    print('hospital 4')