# -*- coding: utf-8 -*-
y1=int(input('digite y1:'))
y2=int(input('digite y2:'))
y3=int(input('digite y3:'))
y4=int(input('digite y4:'))
y5=int(input('digite y5:'))
y6=int(input('digite y6:'))
v1=int(input('digite v1:'))
v2=int(input('digite v2:'))
v3=int(input('digite v3:'))
v4=int(input('digite v4:'))
v5=int(input('digite v5:'))
v6=int(input('digite v6:'))
i=0
cont=0
for i in range(1,99,1):
    if i==y1 or i==y2 or i==y3 or i==y4 or i==y5 or y==y6:
        cont=cont+i
    i=i+1
if cont==3:
    print('terno')
elif cont==4:
    prin('quadra')
elif cont==5:
    print('quina')
elif cont==6:
    print('sena')
elif cont<3:
    print('Azar')