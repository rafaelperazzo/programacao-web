# -*- coding: utf-8 -*-
numero=int(input('digite numero :'))
soma=0
i=0
while numero>0:
    resto=numero%10
    soma=soma+resto*2**i
    i=i+1
    numero=numero//10
print(soma)    


