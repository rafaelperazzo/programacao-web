#-*- coding: utf-8 -*-
V=int(input(' volume : '))
T=int(input(' troca : '))
soma=V
for i in range(0,T,1):
    x=int(input('mudar: '))
    if (soma + x)>100 :
        soma=100
    elif  (soma + x)<0:
        soma=0
    else:
        soma = soma + x
print(soma)