# -*- coding: utf-8 -*-
import math
p=int(input('Digite o primeiro valor: '))
q=int(input('Digite o segundo valor: '))
dividendo=0
quociente=0
cont=0
if p>q:
    while dividendo>0:
        dividendo=p//q
        cont=cont+1
        quociente=p%q
        dividendo=dividendo//quociente
print(cont)