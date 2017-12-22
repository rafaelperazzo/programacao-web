from minha_bib import *
# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
'''
-------------------------------------------------

p1 = float(input('Insira o peso 1: '))
c1 = float(input('Insira o comprimento 1: '))
p2 = float(input('Insira o peso 2: '))
c2 = float(input('Insira o comprimento 2: '))
if (p1*c1) == (p2*c2):
    print('0')
elif (p1*c1) > (p2*c2):
    print('-1')
else:
    print('1')

-------------------------------------------------
'''
'''
#-------------------------------------------------

#MOSTRA TODOS OS NÚMEROS PARES [0,100]
i = 0
while (i<=100):
    if i%2 == 0:
        print(i)
    i += 1
    
#-------------------------------------------------
'''
'''
#-------------------------------------------------

#SOMA TODOS OS NÚMEROS ÍMPARES [O,n[
n = int(input('n: '))
i = 1
cont = 0
while i < n:
    if i%2==1:
        cont = cont + 1
    i = i + 1
print (cont)

#-------------------------------------------------
'''
'''
#-------------------------------------------------

#LOOP INFINITO DE 0
i = 0
while (i<10):
    print(i)
    
#-------------------------------------------------
'''
'''
#-------------------------------------------------

#MOSTRA O QUADRADO DOS NÚMEROS ÍMPARES [0,n]
i = 1
n = int(input('n: '))
while n <= 0:
    n = int(input('n: '))
while i <= n:
    print (i**2)
    i=i+2
    
#-------------------------------------------------
'''
'''
#-------------------------------------------------

#SOMA TODOS OS NÚMERO ÍMPARES DE [0,n[
n = int(input('n: '))
i = 1
cont = 0
while i < n:
    if i%2==1:
        cont = cont + i
    i = i + 1
print (cont)

#-------------------------------------------------
'''
'''
#-------------------------------------------------

#SOMA TODOS OS ALGARISMOS DE N
n = int(input('n: '))
soma = 0
while (n!=0):
    resto = n % 10
    n = (n - resto)//10
    soma = soma + resto
print(soma)
    
#-------------------------------------------------
'''
'''
#-------------------------------------------------

#EXERCÍCIO 11
n = int(input('n: '))
soma = 0
if (10000000 <= n <= 99999999):
    while (n!=0):
        resto = n % 10
        n = (n - resto)//10
        soma = soma + resto
    print(soma)
else:
    print('NAO SEI')

#-------------------------------------------------
'''
'''
#-------------------------------------------------

#FATORIAL DE UM NUMERO POSITIVO
def fatorial(n):
    f = 1
    for i in range(2,n+1,1) :
        f *= i
    return f

while(True):
    n = int(input('n: '))
    if (n >= 0):
        break
f = 1
for i in range(2,n+1,1):
    f *= i
print('%d! = %d' % (n,f))
 
#-------------------------------------------------
'''
'''
#-------------------------------------------------

#AULA DIA 11/10
hello_world()
print(hello_world2())
n1 = int(input('n1: '))
n2 = int(input('n2: '))
print(media(n1,n2))
print(multiplicacao(7,5))
print(fatorial(fatorial(7)))
cronometro(5)
n1 = ler_inteiro()
n2 = ler_inteiro_msg('minha mensagem de input aqui: ')
print(media(n1,n2))
'''

#-------------------------------------------------
#'''
'''
#-------------------------------------------------

#AULA DIA 30/10
notas = []
notas.append(int(input('n: ')))
print(notas)
'''
'''
notas = []
for i in range (0,50,1):
    notas.append(float(input('Insira a nota %d: '%(i+1))))
media = 0
for i in range (0,50,1):
    media += notas[i]/50.0
print(notas)
print(media)
'''
'''
notas = []
n = int(input('Insira o número de notas: '))
while n < 1:
    n = int(input('Insira o número de notas: '))
for i in range (0,n,1):
    notas.append(float(input('Insira a nota %d: '%(i+1))))
media = 0
for i in range (0,n,1):
    media += notas[i]/n
print(notas)
print(media)
'''
a = []
for i in range(1 ,11 ,1):
    a.append(input('Digite o elemento %s: '%(i-1+1)))
for i in range(9 , -1 , -1):
    print(a[i])