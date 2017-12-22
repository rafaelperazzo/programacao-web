 -*- coding: utf-8 -*-
 V=int(input(' volume : '))
 T=int(input(' troca : '))
 soma=V
 for i in range(0,T,1):
     x=int(input('mudar: '))
     soma = soma + x
print(soma)