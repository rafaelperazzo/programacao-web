# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
xc=float(input('coordenada x da cidade'))
x1=float(input('coordenada x do hospital 1'))
x2=float(input('coordenada x do hospital 2'))
x3=float(input('coordenada x do hospital 3'))
x4=float(input('coordenada x do hospital 4'))
yc=float(input('coordenada y da cidade'))
y1=float(input('coordenada y do hospital 1'))
y2=float(input('coordenada y do hospital 2'))
y3=float(input('coordenada y do hospital 3'))
y4=float(input('coordenada y do hospital 4'))
d1=abs(x1-xc)+abs(y1-yc)
d2=abs(x2-xc)+abs(y2-yc)
d3=abs(x3-xc)+abs(y3-yc)
d4=abs(x4-xc)+abs(y4-yc)
if d1<=d2 and d1<=d3 and d1<=d4:
    print('Hospital 1')
elif d2<=d1 and d2<=d3 and d3<=d4:
    print('Hospital 2')
elif d3<=d1 and d3<=d2 and d3<=d4:
    print('Hospital 3')
else:
    print('Hospital 4')