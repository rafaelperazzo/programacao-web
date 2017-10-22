# -*- coding: utf-8 -*-
#************************************************
#FUNÇÃO: CONTAR DÍGITOS
#***********************************************
def contar_digito(x):
    num=0
    while x//10>1:
        x//10
        num=num+1
    return (num)
#************************************************
p=int(input('p: '))
q=0
exp=contar_digito(p)
print (exp)
while q<=p:
    q=int(input('q: '))
while (q//10)>1:
    ult=(q%(10**exp))
    if (ult==p):
        print ('S')
        break
if (ult!=p):
    print ('N')
    

