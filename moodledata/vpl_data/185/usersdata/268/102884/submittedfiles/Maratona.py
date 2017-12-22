# -*- coding: utf-8 -*-
N=int(input('Digite quantos postos terão : '))
M=int(input('Digite o limite do participante: '))
soma =0
cont=0
for i in range(0,N,1):
    
    X9=int(input('Digite a distancia: '))
    y=X9 - soma
    if (y - soma)>M:
        print('N')
        cont=cont+1
        break
    soma=soma + y

if cont==0:
    print('S')
    