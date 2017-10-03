# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a= float(input('Digite um número: '))
b= float(input('Digite outro número: '))
c= float(input('Digite outro número: '))
d= float(input('Digite outro número: '))

#Maior

if a > b and c and d and a :
    print(a, 'é o maior número')
elif b > a and c and d :
    print(b, 'é o maior número')
elif c > a and b and d :
    print(c, 'é o maior número')
elif d > a and b and c :
    print(d, 'é o maior número')
    
#Maior e igual

elif a == b and a and b and c > d :
    print(a, 'é o maior número')
elif a == c and a and c and d > b :
    print(a, 'é o maior número')
elif a == d and a and b and d > c:
    print(a, 'é o maior número')
elif b == c and b and c and d > a:
    print(b, 'é o maior número')
elif b == d and b and d and a > d:
    print(b, 'é o maior número')
elif c == d and c and b and d > a:
    print(c, 'é o maior número')

# iguais
elif a == b and c and d :
    print('Todos os números são iguais')

#Menor

if a < b and c and d and a :
    print(a, 'é o menor número')
elif b < a and c and d :
    print(b, 'é o menor número')
elif c < a and b and d :
    print(c, 'é o menor número')
elif d < a and b and c :
    print(d, 'é o menor número')
    
#Menor e igual

elif a == b and a and b and c < d :
    print(a, 'é o menor número')
elif a == c and a and c and d < b :
    print(a, 'é o menor número')
elif a == d and a and b and d < c:
    print(a, 'é o menor número')
elif b == c and b and c and d < a:
    print(b, 'é o menor número')
elif b == d and b and d and a < d:
    print(b, 'é o menor número')
elif c == d and c and b and d < a:
    print(c, 'é o menor número')
    