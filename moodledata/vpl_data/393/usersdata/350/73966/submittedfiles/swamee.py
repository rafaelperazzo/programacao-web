# -*- coding: utf-8 -*-
import math
g = 9.81
E = 0.000002
f = input( 'Digite f: ')
L = input( 'Digite L: ')
Q = input( 'Digite Q: ')
DeltaH = input( 'Digite DeltaH: ')
v = input( 'Digite v: ')
i = Q**2
x = (((8*f)*L)*i)
s = math.pi
y = (((s**2)*g)*DeltaH)
z = (x / y)
D = z**(1/5)
print('D = %.4f' %D )
a = (4*Q)
b = (((math.pi)*D)*v)
Rey = (a/b)
print('Rey = %.4f' %Rey )
m = (E/(3.7*D))
n = (5.74*(Rey**(9/10)))
t = m + n 
u = math.log10(t)
k = (u**2)
print('k = %.4f' %k )



