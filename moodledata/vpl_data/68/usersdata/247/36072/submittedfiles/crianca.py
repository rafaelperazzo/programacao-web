# -*- coding: utf-8 -*-
p1=float(input('peso da criança da esquerda: '))
c2=float(input('comprimento da gangorra na direita: '))
c1=float(input('comprimento da gangorra na esquerda: '))
p2=float(input('peso da criança da direita: '))
esquerda=p1*c1
direita=p2*c2
if p1*c1==p2*c2:
    print('0')
elif esquerda>direita:
    print(''-1'')
else:
    print('1')
