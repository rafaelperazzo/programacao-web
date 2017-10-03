# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a= float(input('Digite um número: '))
b= float(input('Digite outro número: '))
c= float(input('Digite outro número: '))
d= float(input('Digite outro número: '))

#Maior

if a > b and c and d :
    print(a, 'é o maior número')
elif b > a and c and d :
    print(b, 'é o maior número')
elif c > a and b and d :
    print(c, 'é o maior número')
elif d > a and b and c :
    print(d, 'é o maior número')
    
#Menor

if a < b and c and d :
    print(a, 'é o menor número')
elif b < a and c and d :
    print(a, 'é o menor número')
elif c < a and b and d :
    print(a, 'é o menor número')
elif d < a and b and c :
    print(a, 'é o menor número')