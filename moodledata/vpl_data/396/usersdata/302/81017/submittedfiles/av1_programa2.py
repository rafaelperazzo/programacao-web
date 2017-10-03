# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n = int(input('Primeira aposta: '))
a = int(input('segunda aposta: '))
b = int(input('Terceira aposta: '))
c = int(input('Quarta aposta: '))
d = int(input('Quinta aposta: '))
e = int(input('Sexta aposta: '))
f = int(input('Primeiro sorteado: '))
g = int(input('segundo sorteado: '))
h = int(input('Terceiro sorteado: '))
i = int(input('Quarto sorteado: '))
j = int(input('Quinto sorteado: '))
k = int(input('Sexto sorteado: '))
if (n and a and b and c and d and e) == (f or g or h or i or j or k):
    print('Sena')
if (n and a and b and c and d or e) == (f and g and h and i and j and k):
    print('Quina')

    
    

