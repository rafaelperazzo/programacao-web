# -*- coding: utf-8 -*-
C=int(input('digite C:'))
D=int(input('digite D:'))
cont=0
p=42195
for i in range(1,C+1,1):
    posto=int(input('digite metros:'))
    if posto<=cont:
        cont=cont+D
if cont>=p:
    print('s')
else:
    print('C')
    




















