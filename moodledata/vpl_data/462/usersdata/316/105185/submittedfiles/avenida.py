# -*- coding: utf-8 -*-
m=int(input('digite o numero de quadras no sentido leste-oeste: '))
n=int(input('digite o numero de quadras no sentido norte-sul: '))
for i in range(0,m,1):
    l=[]
    for j in range(0,n,1):
        l.append(float(input('digite o valor da quadra: '))

vc1=([l[0][0]+l[1][0]+l[2][0]+l[3][0]])
vc2=(l[0][1]+l[1][1]+l[2][1]+l[3][1])
vc3=(l[0][2]+l[1][2]+l[2][2]+l[3][2])
vc4=(l[0][3]+l[1][3]+l[2][3]+l[3][3])
if vc1>vc2 and vc1>vc3 and vc1>vc4:
    print([0][1]+l[1][1]+l[2][1]+l[3][1])
elif vc2>vc1 and vc2>vc3 and vc2>vc4:
    if vc1>vc3:
        print(l[0][2]+l[1][2]+l[2][2]+l[3][2])
    else:
        print(l[0][0]+l[1][0]+l[2][0]+l[3][0])
elif vc3>vc1 and vc3>vc2 and vc3>vc4:
    if vc2>vc4:
        print(l[0][3]+l[1][3]+l[2][3]+l[3][3])
    else:
        print(l[0][1]+l[1][1]+l[2][1]+l[3][1])
elif vc4>vc1 and vc4>vc2 and vc4>vc3:
    print(l[0][2]+l[1][2]+l[2][2]+l[3][2])
else:
    print('erro')