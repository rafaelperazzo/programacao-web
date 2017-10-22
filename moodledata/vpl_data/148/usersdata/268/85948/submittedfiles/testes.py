# -*- coding: utf-8 -*-
a= int(input('Digite a : '))
b= int(input('Digite b : '))
c= int(input('Digite c : '))
d= int(input('Digite d : '))
e= int(input('Digite e : '))

X1=a
X2=b
X3=c
X4=d
X5=e

while True:
    if X1>X2 and X1>X3 and X1>X4 and X1>X5:
        print(X1)
        break
    else:
        X1=X2
        X2=X3
        X3=X4
        X4=X5
        X5=X1
while True:
    if X2>X3 and X2>X4 and X2>X5 :
        print(X2)
        break
    else:
        X2=X3
        X3=X4
        X4=X5
        X5=X2
while True:
    if X3>X4 and X4>X5 :
        print(X3)
        break
    else:
        X3=X4
        X4=X5
        X5=X3
while True:
    if X4>X5 :
        print(X4)
        print(X5)
        break
    else:
        X4=X5
        X5=X4