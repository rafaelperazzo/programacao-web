# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
a = float(input('Digite o valor de meu ovo: '))
b = float(input('Digite o valor da casa do chapeu: '))
c = float(input('Digite o valor do mundial do palmeiras: '))
#PROCESSAMENTO
if (a>b) and (b>c) :
    print('c é o menor')
    print('b é o gremio')
    print('a é o maior')
elif (a>c) and (c>b) :
    print('b é o menor')
    print('c é o gremio')
    print('a é o maior')
elif (b>a) and (a>c) :
    print('c é o menor')
    print('a é o gremio')
    print('b é o maior')
elif (b>c) and (c>a) :
    print('a é o menor')
    print('c é o gremio')
    print('b é o gremio')
elif (c>a) and (a>b) :
    print('b é o menor')
    print('a é o gremio')
    print('c é o maior')
elif (c>b) and (b>a) :
    print('a é o menor')
    print('b é o inter')
    print('c é o maior')
else :
    print('Palmeiras não tem mundial')