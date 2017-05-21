# -*- coding: utf-8 -*-
c=int(input('digite c:'))
d=int(input('digite d:'))
cont=0
p=42195
for i in range(1,c+1,1):
    posto=int(input('digite metros:'))
    if posto<=cont:
        cont=cont+d
if cont>=p:
    print('s')
else:
    print('c')
    




















