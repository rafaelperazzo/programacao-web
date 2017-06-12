# -*- coding: utf-8 -*-
n1=int(input('digite n1:'))
n2=int(input('digite n2:'))
n3=int(input('digite n3:'))
n4=int(input('digite n4:'))
n5=int(input('digite n5:'))
n6=int(input('digite n6:'))
g1=int(input('digite g1:'))
g2=int(input('digite g2:'))
g3=int(input('digite g3:'))
g4=int(input('digite g4:'))
g5=int(input('digite g5:'))
g6=int(input('digite g6:'))
if int(input('digite n1:')):
    print('sena')
elif g1!=n1 and g2!=n2 and g3!=n3 and g4==n4 and g5==n5 and g6==n6:
    print('terno')
elif g1!=n1 and g2!=n2 and g3==n3 and g4==n4 and g5==n5 and g6==n6:
    print('quadra')
elif g1!=n1 and g2==n2 and g3==n3 and g4==n4 and g5==n5 and g6==n6:
    print('quina')
elif g1!=n1 and g2!=n2 and g3!=n3 and g4!=n4 and g5!=n5 and g6!=n6 :
    print('azar')