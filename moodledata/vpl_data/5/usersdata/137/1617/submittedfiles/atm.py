# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input(' Digite o valor: '))
a=20
b=10
c=5
d=2
e=1

test1=(valor//a)
a=test1
Stest1=(valor-(test1*20))
test2=(Stest1//b)
b=test2
Stest2=(Stest1-(test2*10))
test3=(Stest2//c)
c=test3
Stest3=(Stest2-(test3*5))
test4=(Stest3//d)
d=test4
Stest4=(Stest3-(test4*2))
test5=int(Stest4//e)
e=test5
print a 
print b
print c
print d
print e
