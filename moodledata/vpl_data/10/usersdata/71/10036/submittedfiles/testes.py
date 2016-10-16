# -*- coding: utf-8 -*-
from __future__ import division
#entrada
p=input("Insira p: ")
q=input("Insira q: ")
#atribuições
contp=0
contq=0
ip=1
iq=1
#contagens de digitos
while p//ip!=0:
    contp=contp+1
    ip=ip*10
while q//iq!=0:
    contq=contq+1
    iq=iq*10
#CP>=cQ
if contq<contp:
    print("Não é subnúmero!")
else:


#teste
    a=q//(10**(contq-contp))
    b=a*(10**(contq-contp))
    c=q-b
    print c
    
    d=q//(10**(contq-contp-1))
    e=(q//(10**(contp+1)))*(10**(contp))
    
    print d
    print e
    
 







