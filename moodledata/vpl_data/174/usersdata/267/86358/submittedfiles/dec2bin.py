# -*- coding: utf-8 -*-
#************************************************
#FUNÇÃO: CONTAR DÍGITOS
#***********************************************
def Contar_digito(x):
    num=0
    while x>0:
        x=x//10
        num=num+1
    return (num)
#************************************************
p=int(input('p: '))
q=0
ex=Contar_digito(p)
print (ex)
while q<=p:
    q=int(input('q: '))
while (q//10)>1:
    ult=(q%(10**ex))
    if (ult==p):
        print ('S')
        break
if (ult!=p):
    print ('N')
    

